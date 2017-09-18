#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This short script checks the serial connections on your RasPi.
# It prints you, at your terminal, the connected USB devices.
# It also informs you about their port-name and their product-ID. 
# RiK4kings: 2017-09-15
# Koenig Engineering GmbH. 

from serial.tools import list_ports

def device_exists():
    try:
        for port in list_ports.comports():
            print port
        return True
    except:
	return False
        print
           

print "\n========= The following devices are connected to my USB: =========\n"
device_exists()
print "\n=========  Thanks for checking. Life long and prosper.   =========\n"
