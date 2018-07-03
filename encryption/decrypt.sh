#!/bin/bash

path=$1
openssl aes-256-cbc -d -in $path -out ${path%.enc} -pass file:$HOME/.PASSWORD
rm $path
if [[ $path =~ ^.+\.tar\.gz\.enc$ ]]; then
  tar xzf ${path%.enc}
  rm ${path%.enc}
fi
