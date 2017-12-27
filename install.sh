#!/bin/bash

#############################
# Wifi Radio install script #
#############################

# update apt-get repository
# apt-get update

#install dependencies
apt-get -qq --yes --force-yes install gcc python-pip

pip install RPi.GPIO pyserial python-mpd2

# setup serial communication

# configure usb soundcard

# start wifi_radio on boot
echo "registering wifi radio as a init.d service"
cp wifi_radio.sh /etc/init.d/
chmod +x /etc/init.d/wifi_radio.sh
update-rc.d wifi_radio.sh defaults



