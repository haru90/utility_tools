#!/bin/bash

openssl aes-256-cbc -e -in $1 -out $1.enc -pass file:$HOME/.PASSWORD
