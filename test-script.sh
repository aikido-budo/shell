≈#!/bin/bash

echo "Welcome to Bob´s burgers"
echo "Please choose what you want to eat:"

meals="Burger Fries"

select option in $meals; do
	echo "You choosed $REPLY"
	echo "The selected meal is $option"
done
