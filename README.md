# My Home Assistant Configuration
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Travis CI][travisci-shield]][travisci]
[![GitHub Activity][commits-shield]][commits]
[![GitHub Last Commit][last-commit-shield]][commits]

![GitHub Stars][stars-shield]
![GitHub Watchers][watchers-shield]
![GitHub Forks][forks-shield]

[![Discord][discord-shield]][discord]

[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee]

## About
This repository stores all of my personal Home Assistant configuration, running all my home automations.

I started using Home Assistant in 2018 but my config was a real mess!
This new repository is a fresh slate, I will rebuild all of my configuration and add new features.

Follow me on this journey and be sure to hit the star above to be notified of changes.

## Host
### VMware ESXi
I currently run a Dell R620 with ESXi installed, im looking at moving to ProxMox in the future.

### docker
I am running HA as a Docker Container using the advanced Hassio install with CentOS as the host OS. Docker makes it easy to upgrade to the latest HA release, while not having to worry about dependencies and python verions.

## Hardware
Currently I only have a small amount of devices, however do plan to expand this during this re-write.
### Smart Devices
* [Ikea TRÅDFRI](https://www.ikea.com/us/en/catalog/categories/departments/lighting/36812/)
* [Shelly1](https://shelly.cloud/shelly1-open-source/)
* [Shelly2.5](https://shelly.cloud/shelly-25-wifi-smart-relay-roller-shutter-home-automation/)
* [Nest Thermostat](https://store.google.com/gb/product/nest_learning_thermostat_3rd_gen) I do not recommend this thermostat but its all I have (soon the API will be shutdown)
### ZigBee
I am currently in the process of getting the Conbee II and will be expanding more once this arrives. I plan on using this with DeCONZ

### Network
* [Ubiquiti USG](https://www.ui.com/unifi-routing/usg/)
* [Ubiquiti UAP-AC-PRO](https://www.ui.com/unifi/unifi-ap-ac-pro/)
* [Ubiquiti US-16-150W](https://www.ui.com/unifi-switching/unifi-switch-16-150w/)
* [Juniper EX2200](https://www.juniper.net/documentation/en_US/release-independent/junos/topics/topic-map/ex2200-system-overview.html)

## Configuration Testing
Each change that is committed will be tested by Travis-CI to check that the build is successful.

## Add-on's
* [A Better Presence](https://github.com/helto4real/hassio-add-ons/tree/master/presence) for better presence detection
* [Mosquitto Broker](https://www.home-assistant.io/addons/mosquitto/) for Shelly MQTT
* [AppDaemon](https://github.com/hassio-addons/addon-appdaemon3) for HADashboard

## Screenshots
Coming Soon...


[maintenance-shield]: https://img.shields.io/maintenance/yes/2019.svg
[license-shield]: https://img.shields.io/github/license/frenck/home-assistant-config.svg

[travisci-shield]: https://travis-ci.org/marksie1988/home-assistant-config.svg?branch=master
[travisci]: https://travis-ci.org/marksie1988/home-assistant-config
[commits-shield]: https://img.shields.io/github/commit-activity/y/marksie1988/home-assistant-config.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/marksie1988/home-assistant-config.svg
[commits]: https://github.com/marksie1988/home-assistant-config/commits/master

[stars-shield]: https://img.shields.io/github/stars/marksie1988/home-assistant-config.svg?style=social&label=Stars
[forks-shield]: https://img.shields.io/github/forks/marksie1988/home-assistant-config.svg?style=social&label=Forks
[watchers-shield]: https://img.shields.io/github/watchers/marksie1988/home-assistant-config.svg?style=social&label=Watchers

[discord-shield]: https://img.shields.io/discord/330944238910963714.svg
[discord]: https://discord.gg/c5DvZ4e

[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg
[buymeacoffee]: https://www.buymeacoffee.com/marksie1988
