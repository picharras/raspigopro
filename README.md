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

##Install service
When raspberry pi run the service 'raspbigopro' run automatic
``` shell
sudo cp raspigopro /etc/init.d/
chmod -x /etc/init.d/raspigopro
sudo update-rc.d raspigopro defaults
```
