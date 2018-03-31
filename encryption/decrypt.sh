#!/bin/bash

openssl aes-256-cbc -d -in $1 -out ${1%.enc} -pass file:$HOME/.PASSWORD
