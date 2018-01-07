#!/bin/bash

#############################
# Wifi Radio install script #
#############################

# update apt-get repository
# apt-get update

# install dependencies
  # apt-get -qq --yes --force-yes install gcc python-pip

  # pip install RPi.GPIO pyserial python-mpd2

# setup serial communication

# configure usb soundcard

# start wifi_radio on boot
echo "registering wifi radio as a init.d service"
cp -f ./setup/wifi_radio.service /lib/systemd/system/wifi_radio.service
sudo chmod 644 /lib/systemd/system/wifi_radio.service

sudo systemctl daemon-reload
sudo systemctl enable wifi_radio.service
