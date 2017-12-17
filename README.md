IP: 192.168.1.19
ssh user: pi/pi

# required dependencies 

- RPi.GPIO
- pyserial
- mpd

## RPi.GPIO

### Install manually
#### Install GCC
$ sudo apt-get update
$ sudo install gcc

#### Install RPi.GPIO
$ https://pypi.python.org/packages/e2/58/6e1b775606da6439fa3fd1550e7f714ac62aa75e162eed29dbec684ecb3e/RPi.GPIO-0.6.3.tar.gz
$ tar zxf RPi.GPIO-0.6.3.tar.gz
$ cd RPi.GPIO-0.6.3
$ sudo python setup.py install

### Install with pip
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

# Starting wifi radio on boot
- make sure $HOME$/debian_init_script/wifi_radio.sh has unix file endings 
- copy file  wifi_radio.sh to /etc/init.d
- change paths in wifi_radio.sh to location to wifi_radio project
- make file wifi_radio.sh executable
- run $sudo update-rc.d wifi_radio.sh defaults (creates symbolic link to /etc/rc?.d)

source: http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/

# Configure USB Soundcard
https://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876

# Set PIN low on Shutdown (to cut off external power supply)
Add following line to /boot/config.txt:
dtoverlay=gpio-poweroff,gpiopin=17,active_low=1

Control relay with gpio pin
http://www.susa.net/wordpress/2012/06/raspberry-pi-relay-using-gpio/

Relay Shutoff Delay
http://www.rbg.ul.schule-bw.de/elektronik/ausschaltverzoegerung.htm

# TODO:
* Read configs from file

# Possible Improvements
* Optimize audio (remove clicking from operations)
* Using mpdlcd: https://github.com/rbarrois/mpdlcd
* Optimize Startup Speed