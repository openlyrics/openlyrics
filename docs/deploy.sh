#!/bin/sh

cd build
if [ -f public_html.tar.gz ]
then
    rm public_html.tar.gz
fi
if [ -d public_html ]
then
    rm -fR public_html
fi
cp -R html public_html
tar -czvf public_html.tar.gz public_html
scp public_html.tar.gz openlyri@openlyrics.info:
ssh openlyri@openlyrics.info 'tar -xzvf public_html.tar.gz; rm public_html.tar.gz; '
