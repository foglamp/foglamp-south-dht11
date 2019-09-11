==================================
fledge-south-dht11 (Raspberry Pi)
==================================

Fledge South Plugin for DHT11 temperature and humidity sensor, for Raspberry Pi.


Hardware
========

A DHT11 plugged directly into the GPIO pins of a Raspberry Pi, the default configuration is to use GPIO4 for the data.


Installation
============
The plugin can be installed with given `requirements.sh <requirements.sh>`_ or with below manual steps:


.. code-block:: bash

   $ pip3 install -Ir python/requirements-dht11.txt --no-cache-dir


Sensor GPIO access
~~~~~~~~~~~~~~~~~~

To access the GPIO pins fledge must be able to access ``/dev/gpiomem``, the default access for this is owner and group read/write.
Either Fledge must be added to the group or the permissions altered to allow Fledge access to the sensor.
