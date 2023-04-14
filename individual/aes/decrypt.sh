#!/usr/bin/env bash

openssl enc -d -aes-256-cbc -in ciphertext -out decrypted_file -pass pass:1672549522
