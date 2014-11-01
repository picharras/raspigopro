raspbygopro
===========

Convert your raspberry pi in one Go Pro

## Requeriments (hardware)
- Raspberry Pi A/B/B+
- Raspberry pi camera
- Switch
- Coffee or beer

## Requeriments (software)
- Last version Raspbian
- Raspberry Pi Camera software. (Instrucctions)[http://www.raspberrypi.org/learning/python-picamera-setup/]

##Install service
When raspberry pi run the service 'raspbigopro' run automatic
``` shell
sudo cp raspigopro /etc/init.d/
chmod -x /etc/init.d/raspigopro
sudo update-rc.d raspigopro defaults
```
