# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

import pytest

from python.foglamp.plugins.south.dht11 import dht11

__author__ = "Praveen Garg"
__copyright__ = "Copyright (c) 2018 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

config = dht11._DEFAULT_CONFIG


def test_plugin_contract():
    # Evaluates if the plugin has all the required methods
    assert callable(getattr(dht11, 'plugin_info'))
    assert callable(getattr(dht11, 'plugin_init'))
    assert callable(getattr(dht11, 'plugin_poll'))
    assert callable(getattr(dht11, 'plugin_shutdown'))
    assert callable(getattr(dht11, 'plugin_reconfigure'))


def test_plugin_info():
    assert dht11.plugin_info() == {
        'name': 'DHT11 GPIO',
        'version': '1.5.0',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': config
    }


@pytest.mark.skip(reason="To be implemented")
def test_plugin_init():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_poll():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_reconfigure():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_shutdown():
    pass
