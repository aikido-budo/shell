#!/bin/bash

#Simple Password Generator

echo "This is a simple password generator"
echo "Please enter the length of the password: "
read PASS_LENGTH
echo "Please enter the number of Passwords: "
read PASS_COUNT

for p in $(seq 1 $PASS_COUNT);
do
	openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done
