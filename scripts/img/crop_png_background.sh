#!/bin/bash

find . -name '*.png' -exec mogrify -trim +repage {} \;
