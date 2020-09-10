# RaspberryPiAquarium

This is a simple Raspberry Pi Aquarium controller written in Python.

Is based in 2 main things, a Python script to manage a relay and a crontab schedule to control the Python execution over the day.

## Python controller
https://github.com/u915/RaspberryPiAquarium/tree/master/Python

## Crontab schedule
https://github.com/u915/RaspberryPiAquarium/tree/master/Crontab

## Circuit scheme
![alt text](https://github.com/u915/RaspberryPiAquarium/blob/master/Circuit/circuit.png "Circuit")

Made with https://www.circuit-diagram.org the circuit scheme is also included.

## Parts

Tested with 2 Raspberry Pi models:

Raspberry Pi model 3 B 1.2 and an old Raspberry Pi model 1 from 2011.

Currently i am using the 2011 Raspberry Pi with the USB Wifi Adapter Edimax, because the Pi does not have a RTC clock module so is just connected the Pi board to the Wifi to refresh the date by NTP and to be managed by SSH. 

#### Edimax EW-7811UN 150 MB/s

https://www.amazon.es/gp/product/B003MTTJOY

#### Relay 

https://www.amazon.es/gp/product/B078Q326KT

#### 3D printed case from Thingiverge

https://www.thingiverse.com/thing:4088536






