A FogLAMP South plugin for the DHT11
====================================

A simple sensor plugin for a DHT11 temperature and humidity sensor. This
plugin uses the DHT11 library available from Adafruit

Hardware
========

A DHT11 pluged directly into the GPIO pins of a Raspberry Pi, the default
configuration is to use GPIO4 for the data from the DHT11.


Installation
============

Plugin for a DHT11 temperature and humidity sensor attached directly to the GPIO pins of a Raspberry Pi.

This plugin uses the Adafruit DHT library, to install this, perform the following steps:

.. code-block:: bash

        git clone https://github.com/adafruit/Adafruit_Python_DHT.git
        cd Adafruit_Python_DHT
        sudo apt-get install build-essential python-dev
        sudo python setup.py install

To access the GPIO pins foglamp must be able to access :bash:`/dev/gpiomem`, the default access for this is owner and group read/write.
Either FogLAMP must be added to the group or the permissions altered to allow FogLAMP access to the device.


