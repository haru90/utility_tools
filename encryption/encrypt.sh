#!/bin/bash

path=$1
if [ -f $path ]; then
  openssl aes-256-cbc -e -in $path -out $path.enc -pass file:$HOME/.PASSWORD
  rm $path
elif [ -d $path ]; then
  tar czf $path.tar.gz $path
  tgz_path=$path.tar.gz
  openssl aes-256-cbc -e -in $tgz_path -out $tgz_path.enc -pass file:$HOME/.PASSWORD
  rm -rf $path
  rm $tgz_path
else
  echo "Error: $path is not a file or directory"
fi
