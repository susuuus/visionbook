1. Authentication relies on `oauth2-proxy` and `GitHub`.
2. After installation, add the following block to `nginx` configuration:
```
location /cv_book {
        auth_request /oauth2/auth;
        error_page 401 = /oauth2/start?rd=$request_uri;
        alias /home/shenshen/code/cv_book/_book;
        try_files $uri $uri/ =404;
    }
    location = /oauth2/start {
        proxy_pass http://127.0.0.1:4180;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    location = /oauth2/auth {
        internal;
        proxy_pass http://127.0.0.1:4180; # Adjust if `oauth2-proxy` is running on a different port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass_request_body off;
        proxy_set_header Content-Length "";
    }

    location = /oauth2/sign_in {
        proxy_pass http://127.0.0.1:4180;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    location = /oauth2/callback {
        proxy_pass http://127.0.0.1:4180; # Ensure this points to where oauth2-proxy is listening
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

```
3. add the following config file `/etc/oauth2-proxy.cfg`:
```
email_domains=["*"]
upstreams = [ "http://127.0.0.1:8080" ]  # This should point to where Nginx is hosting your application
client_id = "ID"
client_secret = "SECRET"
provider = "github"
cookie_secret ="some hashed string"
cookie_secure = true
redirect_url = "https://shenshen.mit.edu/oauth2/callback"
```

4. make `oauth2-proxy` a systemd service, and control user access. In particular, add `/etc/systemd/system/oauth2-proxy.service`

```
[Unit]
Description=OAuth2 Proxy
After=network.target

[Service]
User=nobody
Group=nogroup
Restart=on-failure
ExecStart=/usr/local/bin/oauth2-proxy --config /etc/oauth2-proxy.cfg --github-user shensquared,abtorralba,phillipi
[Install]
WantedBy=multi-user.target
```
