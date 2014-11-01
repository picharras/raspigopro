RaspbiGoPro
===========

Convert your raspberry pi in one awesome GoPro camera

## Requirements (hardware)
- Raspberry Pi A/B/B+
- Raspberry pi camera
- Switch
- Coffee or beer

## Requirements (software)
Most of the software listed here can be installed from aptitude or apt.
- Last version Raspbian
- GPIO software. [Instructions](http://raspberrypi.stackexchange.com/questions/8220/how-to-correctly-install-the-python-rpi-gpio-library)
- Raspberry Pi Camera software. [Instructions](http://www.raspberrypi.org/learning/python-picamera-setup/)
- Git. [Instructions](http://git-scm.com/)

## Instructions
Connect switch to 5v and GPIO 17 as shown in the diagram below:
![Circuit](https://dl.dropboxusercontent.com/u/978896/raspberrypi-switch.png)

Log in to your Raspberry Pi through ssh
``` shell
$ ssh pi@raspberry-pi-IP
```

Clone the 'raspigopro' repo and go to 'raspbigopro' folder
``` shell
$ git clone https://github.com/picharras/raspigopro.git
$ cd raspigopro
```
Create the 'videos' folder if not exist
``` shell
$ mkdir videos
```

Make executable 'raspigopro.py' file
``` shell
$ sudo chmod +x raspigopro.py
```
Make sure the 'raspigopro' service will run every time you start your Raspberry Pi. Before, you must edit it "DIR=" to make sure indicates the correct path.
``` shell
$ sudo cp raspigopro /etc/init.d/
$ sudo chmod +x /etc/init.d/raspigopro
$ sudo update-rc.d raspigopro defaults
```

Reboot your pi
``` shell
$ sudo reboot
```
Now you can record video pushing the switch(LED turn on) and stop record video pushing again(LED turn off). Enjoy!


[![How to works](http://img.youtube.com/vi/V8kMGmvkRow/0.jpg)](https://www.youtube.com/watch?v=V8kMGmvkRow)
