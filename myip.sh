#!/bin/bash

echo "get public IP via DNS request"
echo "-----------------------------"
echo "Provider IP is: "

dig +short myip.opendns.com @resolver1.opendns.com


