#!/bin/bash

xterm -e 'redshift -O 3800'
xterm -e 'sudo apt update && sudo apt upgrade && sudo systemctl disable bluetooth.service && sudo systemctl stop bluetooth.service'
xterm -e 'cp -f ~/htoprc ~/.config/htop/'
