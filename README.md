# Raspberry-PI Wifi-Radio
My attempt to build a retro wifi radio from scratch using a raspberry pi, arduinos encased in an old radio Loewe Opta Bella-Luxus 2711W. I started the project in 2014 and worked on it sporadically, when I had time and motivation.

# Getting started
## Prerequisites
You will need the following hardware if you want to rebuilt this radio as it is:
* 1 x raspberry pi (I used a Raspberry Pi Model B Rev 2.0)
* 2 x Arduino Pro Mini
* 1 x hd44780 4x20 LCD Display
* 2 x push-button rotary encoders
* 1 x 5V/3.3V Logic Level Converter
* 1 x PAM8403 3W Amplifier
* 2 x 3 Ohm Speakers
* 1 x wifi dongle
* 1 x 25 Watt power source
* 1 x USB Soundcard (optional)
* Cables and passive components

The hardware used in the current setup is not optimal, as the project started with some components I had laying around and grew over time. Feel free to change it to your taste.

The following schematic shows, how the hardware is tied together:
![Radio schematic](docs/Wifi_Radio_Wiring.jpg?raw=true "Radio schematic")

## Installation
The project is quite hardware dependent, so you will have to do some configuration up front. [This](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md) guide will help you, if you don't know how to connect your RPI to a wifi and [this](https://www.raspberrypi.org/documentation/remote-access/ssh/guide) one to set up SSH access. As the GPIO pins of the raspberry pi are limited, one of the arduinos is communicating to the RPI over serial communication. By default, the RPIs serial port is configured for console input/output. [This](http://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/) guide shows you how to disable it for Raspbian and [this](http://www.hobbytronics.co.uk/raspberry-pi-serial-port) one if you intend to run the radio on debian.

One of my goals for the radio was to completely cut off the power supply if the RPI shuts down. I did not find any suitable solutions so I designed a circuit for this purpose. You can find the schematics in the /docs folder. The RPI can be configured to set a pin from high to low if it shuts down. The curcuit probes this pin and cuts of power, if it is set to low. The following line has to be added to `/boot/config.txt` to enable this functionality:

    dtoverlay=gpio-poweroff,gpiopin=17,active_low=1

It is not required, but if you intend to use a USB soundcard you can check out this [guide](https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876) guide by Jordan Merrick.

With all the hardware setup being done, we finally can install the software via pip:

    $> pip install wifi_radio

### Running the tests
To run the tests simply navigate to the root of the project and run:

    $> python -m unittest discover

# Acknowledgments
The RPI, python and other communities were valueable sources of knowledge and inspiration. The following were particularly useful. Thanks guys!
* Inspiration
  * [Sheldon Hartling](http://usualpanic.com/2013/05/raspberry-pi-internet-radio/)
* LCD
  * [Matt Hawkins - LCD Control](http://www.raspberrypi-spy.co.uk/2012/08/20x4-lcd-module-control-using-python/)
  * [Alan Aufderheide - LCD Menu](https://github.com/aufder/RaspberryPiLcdMenu/blob/master/lcdmenu.py)
* Deployment and configuration
  * [Matt Hawkins - Start radio at boot](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
  * [Jordan Merrick - USB Soundcard Configuration](https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876)
  * [setup.py with systemd registration](https://github.com/python-diamond/Diamond/blob/master/setup.py)
  * [Timezone settings for debian](https://d0m.me/2008/07/21/debian-linux-zeitzone-und-uhr-umstellen-deutschlandgermany/)
  
