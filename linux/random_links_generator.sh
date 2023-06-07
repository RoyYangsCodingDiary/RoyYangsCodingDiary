#!/bin/bash

echo "Enter a number:"
read number

links_file="/home/cole/Documents/scripts/links.txt"
links=($(cat "$links_file"))

num_links=${#links[@]}

if ! [[ "$number" =~ ^[0-9]+$ ]]; then
echo "Error: Invalid input. Please enter a valid number."
exit 1
fi

if [ "$number" -gt "$num_links" ]; then
echo "Error: The number entered is greater than the available links."
exit 1
fi

used_indices=()

tab_command=""

for ((i=0; i<number; i++))
do
while true
do
random_index=$RANDOM
let "random_index %= num_links"
if [[ ! " ${used_indices[@]} " =~ " ${random_index} " ]]; then
used_indices+=($random_index)
break
fi
done

chosen_link=${links[$random_index]}
tab_command+="--new-tab "$chosen_link" "
done

browser="librewolf"

if ! command -v "$browser" >/dev/null; then
echo "Error: $browser is not installed or not found in the system PATH."
exit 1
fi

"$browser" $tab_command

exit
