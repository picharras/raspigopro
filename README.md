raspbygopro
===========

Convert your raspberry pi in one Go Pro

## Requeriments (hardware)
- Raspberry Pi A/B/B+
- Raspberry pi camera
- Switch
- Coffee or beer

## Requeriments (software)
La mayoria del software aqui listado se puede instalar tambien desde aptitude o apt.
- Last version Raspbian
- GPIO software. [Instructions](http://raspberrypi.stackexchange.com/questions/8220/how-to-correctly-install-the-python-rpi-gpio-library)
- Raspberry Pi Camera software. [Instructions](http://www.raspberrypi.org/learning/python-picamera-setup/)
- Git. [Instructions](http://git-scm.com/)

##Instructions
Log in to your Raspberry Pi through ssh
``` shell
ssh pi@raspberry-pi-IP
```

Clone this repo
``` shell
git clone https://github.com/picharras/raspigopro.git
cd raspigopro
```
Create the 'videos' folder if not exist
``` shell
mkdir videos
```

Make executable 'raspigopro.py' file
``` shell
sudo chmod +x raspigopro.py
```
Make sure the 'raspigopro' service will run every time you start your Raspberry Pi
``` shell
sudo cp raspigopro /etc/init.d/
sudo chmod -x /etc/init.d/raspigopro
sudo update-rc.d raspigopro defaults
```
