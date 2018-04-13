# Raspberry-PI Wifi-Radio
My attempt to build a retro wifi radio from scratch using a raspberry pi, arduinos and an old radio Loewe Opta Bella-Luxus 2711W case. I started the project in 2014 and worked on it sporadically, when I had time and motivation.

## Getting started
### Prerequisites
You will need the following hardware if you want to rebuilt this radio as it is:
* 1 x raspberry pi (I used a Raspberry Pi Model B Rev 2.0)
* 2 x Arduino Pro Mini
* 1 x hd44780 4x20 LCD Display
* 2 x push-button rotary encoders
* 1 x 5V/3.3V Logic Level Converter
* 1 x PAM8403 3W Amplifier
* 1 x USB Soundcard (optional)
* 1 x wifi dongle
* 1 x 25 Watt power source

The hardware used in the current setup is not optimal, as the project started with some components I had laying around and grew over time. Feel free to change it to your taste.

The following schematic shows, how the hardware is tied together:
![Radio schematic](docs/Wifi_Radio_Wiring_Steckplatine.jpg?raw=true "Radio schematic")

### Installation

#### Prepare OS
* [Configure Wifi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
* [Enable SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

#### Install Project

    $> pip install wifi_radio

### Running the tests
To run the tests simply navigate to the root of the project and run:

    $> python -m unittest discover

# Acknowledgments
* Inspiration
  * [Sheldon Hartling](http://usualpanic.com/2013/05/raspberry-pi-internet-radio/)
* LCD
  * LCD Control: [Matt Hawkins](http://www.raspberrypi-spy.co.uk/2012/08/20x4-lcd-module-control-using-python/)
  * LCD Menu: [Alan Aufderheide](https://github.com/aufder/RaspberryPiLcdMenu/blob/master/lcdmenu.py)
* Infrastructure
  * [Start radio at boot](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
  * [Timezone settings for debian](https://d0m.me/2008/07/21/debian-linux-zeitzone-und-uhr-umstellen-deutschlandgermany/)
  * [USB Soundcard Configuration](https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876)


# Remove

# install package to systemd
## Tutorials
https://weblog.christoph-egger.org/Installing_a_python_systemd_service_.html
https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer/systemd-writing-and-enabling-a-service

## Projects with init scripts
* https://github.com/python-diamond/Diamond/blob/master/setup.py
* https://github.com/liftoff/GateOne/blob/master/setup.py

## Debian packaging
https://wiki.debian.org/Python/LibraryStyleGuide

- RPi.GPIO
- pyserial
- mpd

## RPi.GPIO

### Install manually
#### Install GCC
$ sudo apt-get update
$ sudo install gcc

#### Install RPi.GPIO
$ sudo apt-get install python-pip 
$ sudo pip install RPi.GPIO

## pyserial
$ sudo pip install pyserial

## mpd
source: https://github.com/Mic92/python-mpd2

$ sudo pip install python-mpd2

# Setup Serial Communication
The Serial Login Screen has to be disabled to use the serial ports for communication with the arduino board-
Check [this](http://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/) tutorial if you use raspbian
Check [this](http://www.hobbytronics.co.uk/raspberry-pi-serial-port) tutorial if you use debian


# Configure USB Soundcard
https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876

# Set PIN low on Shutdown (to cut off external power supply)
Add following line to /boot/config.txt:
dtoverlay=gpio-poweroff,gpiopin=17,active_low=1

Control relay with gpio pin
http://www.susa.net/wordpress/2012/06/raspberry-pi-relay-using-gpio/

Relay Shutoff Delay
http://www.rbg.ul.schule-bw.de/elektronik/ausschaltverzoegerung.htm

## Using virtualenv
http://docs.python-guide.org/en/latest/dev/virtualenvs/