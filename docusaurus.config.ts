import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";
import remarkMath from "remark-math";
// import rehypeKatex from "rehype-katex";
import rehypeMathjax from "rehype-mathjax";
import "dotenv/config";
const config: Config = {
    title: "Foundations of Computer Vision",
    staticDirectories: ["public", "static"],
    tagline: "Foundations of Computer Vision",
    favicon: "img/favicon.ico",

    // Set the production url of your site here
    url: "https://introml.mit.edu",
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: process.env.BASEURL || "",

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: "shensquared", // Usually your GitHub org/user name.
    projectName: "cv_book", // Usually your repo name.

    onBrokenLinks: "warn",
    onBrokenMarkdownLinks: "warn",
    plugins: [require.resolve("docusaurus-lunr-search")],
    // Even if you don't use internationalization, you can use this field to set
    // useful metadata like html lang. For example, if your site is Chinese, you
    // may want to replace "en" with "zh-Hans".
    i18n: {
        defaultLocale: "en",
        locales: ["en"],
    },

    presets: [
        [
            "classic",
            {
                docs: {
                    admonitions: {
                        keywords: ["codebox", "example"],
                        extendDefaults: true,
                    },
                    path: "docs",
                    remarkPlugins: [remarkMath],
                    rehypePlugins: [
                        [
                            rehypeMathjax,
                            {
                                tex: {
                                    inlineMath: [
                                        ["$", "$"],
                                        ["\\(", "\\)"],
                                    ],
                                    displayMath: [
                                        ["$$", "$$"],
                                        ["\\[", "\\]"],
                                    ],
                                    processEscapes: true,
                                    tags: "ams",
                                },
                            },
                        ],
                    ],
                    sidebarPath: "./sidebars.ts",
                    routeBasePath: "book",
                    editUrl:
                        "https://github.com/shensquared/introml-notes/blob/main",
                },
                blog: false,
                theme: {
                    customCss: "./src/css/custom.css",
                },
            } satisfies Preset.Options,
        ],
    ],
    // stylesheets: [
    //     {
    //         href: "https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css",
    //         type: "text/css",
    //         integrity:
    //             "sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM",
    //         crossorigin: "anonymous",
    //     },
    // ],
    scripts: [
        {
            src: "https://hypothes.is/embed.js",
            async: true,
        },
        {
            // src: "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.min.js",
            src: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
            async: true,
        },
    ],
    themeConfig: {
        // Replace with your project's social card
        image: "img/390.png",
        navbar: {
            title: "Foundations of Computer Vision",
            // logo: {
            //     alt: "introml_logo",
            //     src: "img/390.png",
            // },
            items: [
                {
                    type: "docSidebar",
                    sidebarId: "Sidebar",
                    position: "left",
                    label: "book",
                },
                {
                    href: "https://github.com/shensquared/introml-notes",
                    className: "header-github-link",
                    position: "right",
                },
            ],
        },
        docs: {
            sidebar: {
                hideable: true,
                autoCollapseCategories: false,
            },
        },
        prism: {
            theme: prismThemes.github,
            darkTheme: prismThemes.dracula,
        },
    } satisfies Preset.ThemeConfig,
};

export default config;
