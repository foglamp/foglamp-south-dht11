==================================
foglamp-south-dht11 (Raspberry Pi)
==================================

FogLAMP South Plugin for DHT11 temperature and humidity sensor, for Raspberry Pi.


Hardware
========

A DHT11 pluged directly into the GPIO pins of a Raspberry Pi, the default configuration is to use GPIO4 for the data.


Installation
============


Create Debian Package
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ ./make_deb help
    make_deb help [clean|cleanall]
    This script is used to create the Debian package of foglamp dht11 plugin

    Arguments:
     help     - Display this help text
     clean    - Remove all the old versions saved in format .XXXX
     cleanall - Remove all the versions, including the last one

``./make_deb`` will create the debian package inside ``packages/build/``.


Pre Debian Package Install
~~~~~~~~~~~~~~~~~~~~~~~~~~

This plugin uses the Adafruit_Python_DHT python package. There is a known issue with pip package.

https://github.com/adafruit/Adafruit_Python_DHT/issues/99

Hence to install this, perform the following steps:

.. code-block:: bash

   git clone https://github.com/adafruit/Adafruit_Python_DHT.git
   cd Adafruit_Python_DHT
   sudo apt-get install build-essential python3-dev
   sudo python3 setup.py install


Sensor GPIO access
~~~~~~~~~~~~~~~~~~

To access the GPIO pins foglamp must be able to access ``/dev/gpiomem``, the default access for this is owner and group read/write.
Either FogLAMP must be added to the group or the permissions altered to allow FogLAMP access to the sensor.


Install Debian Package
~~~~~~~~~~~~~~~~~~~~~~

Make sure FogLAMP is installed and running.

.. code-block:: console

  $ sudo systemctl status foglamp.service


Once you have created the debian package, install it using the ``apt`` command. Move the package to the apt cache directory
i.e. ``/var/cache/apt/archives``.

.. code-block:: console

  $ sudo cp foglamp-south-dht11-1.0.1.deb /var/cache/apt/archives/.
  $ sudo apt install /var/cache/apt/archives/foglamp-south-dht11-1.0.1.deb


Check the newly installed package:

.. code-block:: console

  $ sudo dpkg -l | grep foglamp-south-dht11
  ii  foglamp-south-dht11    1.0.1    armhf    South plugin for the DHT1

Check foglamp service status for foglamp-south-dht11, it should list it as a south service:

.. code-block:: console

  $ sudo systemctl status foglamp.service
  ...
  ...
  CGroup: /system.slice/foglamp.service
           |- ....
           ├─/bin/sh services/south --port=43926 --address=127.0.0.1 --name=DHT11
           └─python3 -m foglamp.services.south --port=43927 --address=127.0.0.1 --name=DHT11
