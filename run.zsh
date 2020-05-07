#!/bin/zsh

echo "exit()" | python3 # clear python terminal
clear
# Following the command is the test file number
if [ $1 = 1 ]
then
    cat input1.txt | python3 /Users/joshwinebrener/my_code/RubiksSolver/rubiks.py
else
    python3 /Users/joshwinebrener/my_code/RubiksSolver/rubiks.py
fi