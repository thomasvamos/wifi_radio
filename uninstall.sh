#!/bin/bash

systemctl stop wifi_radio.service
systemctl disable wifi_radio.service
rm -f /etc/systemd/system/multi-user.target.wants/wifi_radio.service
rm -f /lib/systemd/system/wifi_radio.service
systemctl daemon-reload
systemctl reset-failed