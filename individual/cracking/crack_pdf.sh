#!/usr/bin/env bash

hashcat -m 10700 -a 0 --force -O -w3 --opencl-device-types 1,2 pdf_4_hashcat rockyou.txt 