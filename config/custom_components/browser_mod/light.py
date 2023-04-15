import logging
from datetime import datetime

from homeassistant.const import STATE_UNAVAILABLE, STATE_ON, STATE_OFF
from homeassistant.components.light import LightEntity, SUPPORT_BRIGHTNESS

from .helpers import setup_platform, BrowserModEntity

PLATFORM = 'light'

async def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    return setup_platform(hass, config, async_add_devices, PLATFORM, BrowserModLight)

class BrowserModLight(LightEntity, BrowserModEntity):
    domain = PLATFORM

    def __init__(self, hass, connection, deviceID, alias=None):
        super().__init__(hass, connection, deviceID, alias)
        self.last_seen = None

    def updated(self):
        self.last_seen = datetime.now()
        self.schedule_update_ha_state()

    @property
    def state(self):
        if not self.connection.connection:
            return STATE_UNAVAILABLE
        return STATE_OFF if self.data.get('blackout', False) else STATE_ON

    @property
    def is_on(self):
        return not self.data.get('blackout', False)

    @property
    def device_state_attributes(self):
        return {
                "type": "browser_mod",
                "deviceID": self.deviceID,
                "last_seen": self.last_seen,
                }

    @property
    def supported_features(self):
        return SUPPORT_BRIGHTNESS if self.data.get('brightness', False) else 0

    def turn_on(self, **kwargs):
        self.connection.send("no-blackout", **kwargs)

    def turn_off(self, **kwargs):
        self.connection.send("blackout")
