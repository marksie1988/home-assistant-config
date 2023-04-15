"""API Handler for hacs_config"""
import voluptuous as vol
from homeassistant.components import websocket_api

from custom_components.hacs.share import get_hacs


@websocket_api.async_response
@websocket_api.websocket_command({vol.Required("type"): "hacs/config"})
async def hacs_config(hass, connection, msg):
    """Handle get media player cover command."""
    hacs = get_hacs()
    config = hacs.configuration

    content = {
        "frontend_mode": config.frontend_mode,
        "frontend_compact": config.frontend_compact,
        "onboarding_done": config.onboarding_done,
        "version": hacs.version,
        "frontend_expected": hacs.frontend.version_expected,
        "frontend_running": hacs.frontend.version_running,
        "dev": config.dev,
        "debug": config.debug,
        "country": config.country,
        "experimental": config.experimental,
        "categories": hacs.common.categories,
    }
    connection.send_message(websocket_api.result_message(msg["id"], content))
