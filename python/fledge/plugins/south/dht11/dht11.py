# -*- coding: utf-8 -*-

# FLEDGE_BEGIN
# See: http://fledge.readthedocs.io/
# FLEDGE_END

""" Plugin for a DHT11 temperature and humidity sensor attached directly to the GPIO pins of a Raspberry Pi. """

from datetime import datetime, timezone
import copy
import uuid
import logging

# TODO: https://github.com/adafruit/Adafruit_Python_DHT/issues/99
import Adafruit_DHT

from fledge.common import logger
from fledge.plugins.common import utils
from fledge.services.south import exceptions


__author__ = "Mark Riddoch"
__copyright__ = "Copyright (c) 2018 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

_DEFAULT_CONFIG = {
    'plugin': {
        'description': 'DHT11 South Plugin',
        'type': 'string',
        'default': 'dht11',
        'readonly': 'true'
    },
    'assetName': {
        'description': 'Asset name',
        'type': 'string',
        'default': "dht11",
        'order': "1",
        'displayName': 'Asset Name'
    },
    'gpioPin': {
        'description': 'The GPIO pin into which the DHT11 data pin is connected', 
        'type': 'integer',
        'default': '4',
        'order': '3',
        'displayName': 'GPIO Pin'
    }

}

_LOGGER = logger.setup(__name__)
""" Setup the access to the logging system of Fledge """
_LOGGER.setLevel(logging.INFO)


def plugin_info():
    """ Returns information about the plugin.

    Args:
    Returns:
        dict: plugin information
    Raises:
    """

    return {
        'name': 'DHT11 GPIO',
        'version': '1.7.0',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }


def plugin_init(config):
    """ Initialise the plugin.

    Args:
        config: JSON configuration document for the plugin configuration category
    Returns:
        handle: JSON object to be used in future calls to the plugin
    Raises:
    """

    handle = copy.deepcopy(config)
    return handle


def plugin_poll(handle):
    """ Extracts data from the sensor and returns it in a JSON document as a Python dict.

    Available for poll mode only.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        returns a sensor reading in a JSON document, as a Python dict, if it is available
        None - If no reading is available
    Raises:
        DataRetrievalError
    """

    try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, handle['gpioPin']['value'])
        if humidity is not None and temperature is not None:
            time_stamp = utils.local_timestamp()
            readings = {'temperature': temperature, 'humidity': humidity}
            wrapper = {
                    'asset':     handle['assetName']['value'],
                    'timestamp': time_stamp,
                    'key':       str(uuid.uuid4()),
                    'readings':  readings
            }
        else:
            raise exceptions.DataRetrievalError
    except Exception:
        raise
    else:
        return wrapper


def plugin_reconfigure(handle, new_config):
    """ Reconfigures the plugin, it should be called when the configuration of the plugin is changed during the
        operation of the south service.
        The new configuration category should be passed.

    Args:
        handle: handle returned by the plugin initialisation call
        new_config: JSON object representing the new configuration category for the category
    Returns:
        new_handle: new handle to be used in the future calls
    Raises:
    """
    _LOGGER.info("Old config for DHT11 plugin {} \n new config {}".format(handle, new_config))

    new_handle = copy.deepcopy(new_config)
    return new_handle


def plugin_shutdown(handle):
    """ Shutdowns the plugin doing required cleanup, to be called prior to the service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
    Raises:
    """
    _LOGGER.info("DHT11 Poll plugin shutdown")
