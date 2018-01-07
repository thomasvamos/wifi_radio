#!/bin/bash

#############################
# Wifi Radio install script #
#############################

# set correct timezone
sudo echo "Europe/Berlin" > /etc/timezone
sudo dpkg-reconfigure tzdata

# update apt-get repository
# apt-get update

# install dependencies
  # apt-get -qq --yes --force-yes install gcc python-pip

  # pip install RPi.GPIO pyserial python-mpd2

# setup serial communication

# configure usb soundcard

# start wifi_radio on boot
echo "registering wifi radio as a init.d service"
cp -f ./install/wifi_radio.service /lib/systemd/system/wifi_radio.service
sudo chmod 644 /lib/systemd/system/wifi_radio.service

sudo systemctl daemon-reload
sudo systemctl enable wifi_radio.service

# legacy
# cp wifi_radio.sh /etc/init.d/
# chmod +x /etc/init.d/wifi_radio.sh
# update-rc.d wifi_radio.sh defaults



