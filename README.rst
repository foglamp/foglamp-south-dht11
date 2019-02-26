==================================
foglamp-south-dht11 (Raspberry Pi)
==================================

FogLAMP South Plugin for DHT11 temperature and humidity sensor, for Raspberry Pi.


Hardware
========

A DHT11 plugged directly into the GPIO pins of a Raspberry Pi, the default configuration is to use GPIO4 for the data.


Installation
============
On Rpi the packages can be installed with given `requirements.sh <requirements.sh>`_ or with below manual steps:


.. code-block:: bash

   $ sudo apt install -y wiringpi
   $ pip3 install -Ir python/requirements-dht.txt --no-cache-dir

Create Debian Package
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ ./make_deb help
    make_deb [clean|cleanall]
    This script is used to create the Debian package of foglamp dht11 plugin

    Arguments:
     clean    - Remove all the old versions saved in format .XXXX
     cleanall - Remove all the versions, including the last one

``./make_deb`` will create the debian package inside ``packages/build/``.


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

  $ sudo cp foglamp-south-dht11-1.0.0-armhf.deb /var/cache/apt/archives/.
  $ sudo apt install /var/cache/apt/archives/foglamp-south-dht11-1.0.0-armhf.deb


Check the newly installed package:

.. code-block:: console

  $ sudo dpkg -l | grep foglamp-south-dht11


Check foglamp service status for foglamp-south-dht11, it should list it as a south service:

.. code-block:: console

  $ sudo systemctl status foglamp.service
  ...
  ...
  CGroup: /system.slice/foglamp.service
           |- ....
           └─python3 -m foglamp.services.south --port=43927 --address=127.0.0.1 --name=dht11
