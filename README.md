# My Home Assistant Configuration

![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Build Status][gitlab-shield]][gitlab]
[![GitHub Activity][commits-shield]][commits]
[![GitHub Last Commit][last-commit-shield]][commits]

![GitHub Stars][stars-shield]
![GitHub Watchers][watchers-shield]
![GitHub Forks][forks-shield]

[![Discord][discord-shield]][discord]

[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee]

## About

This repository stores my personal Home Assistant configuration.

I started using Home Assistant in 2018 but my config was a real mess!
This new repository is a fresh slate, I will rebuild all of my configuration
and add new features.

Follow me on this journey and be sure to hit the :star:

## Host

### VMware ESXi

I currently run a Dell R620 with ESXi installed,
I'm looking at moving to ProxMox in the future.

### docker

I am running HA as a Docker Container using the advanced Hassio
install with CentOS as the host OS.
Docker makes it easy to upgrade to the latest HA release,
while not having to worry about dependencies and python verions.

## Hardware

Currently I only have a small amount of devices,
however do plan to expand this during this re-write.

### Smart Devices

* [Ikea TRÅDFRI](https://www.ikea.com/us/en/catalog/categories/departments/lighting/36812/)
* [Shelly1](https://shelly.cloud/shelly1-open-source/)
* [Shelly2.5](https://shelly.cloud/shelly-25-wifi-smart-relay-roller-shutter-home-automation/)
* [Nest Thermostat](https://store.google.com/gb/product/nest_learning_thermostat_3rd_gen)
  * I do not recommend this thermostat but its all I have (soon the API will be shutdown)

### ZigBee

I have just redeployed Hassio with the Conbee II attached,
I have setup DeConz for connecting the devices to HA.
This currently controls my Ikea TRÅDFRI lights

### Network

* [Ubiquiti USG](https://www.ui.com/unifi-routing/usg/)
* [Ubiquiti UAP-AC-PRO](https://www.ui.com/unifi/unifi-ap-ac-pro/)
* [Ubiquiti US-16-150W](https://www.ui.com/unifi-switching/unifi-switch-16-150w/)
* [Juniper EX2200](https://www.juniper.net/documentation/en_US/release-independent/junos/topics/topic-map/ex2200-system-overview.html)

## Add-on's

* [A Better Presence](https://github.com/helto4real/hassio-add-ons/tree/master/presence)
  * for better presence detection
* [Mosquitto Broker](https://www.home-assistant.io/addons/mosquitto/)
  * for Shelly MQTT
* [AppDaemon](https://github.com/hassio-addons/addon-appdaemon3)
  * for HADashboard

## Screenshot

Coming Soon...

[maintenance-shield]: https://img.shields.io/maintenance/yes/2019.svg
[license-shield]: https://img.shields.io/github/license/frenck/home-assistant-config.svg

[gitlab-shield]: https://gitlab.com/marksie1988/home-assistant-config/badges/master/pipeline.svg
[gitlab]: https://gitlab.com/marksie1988/home-assistant-config/pipelines
[commits-shield]: https://img.shields.io/github/commit-activity/y/marksie1988/home-assistant-config.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/marksie1988/home-assistant-config.svg
[commits]: https://github.com/marksie1988/home-assistant-config/commits/master

[stars-shield]: https://img.shields.io/github/stars/marksie1988/home-assistant-config.svg?style=social&label=Stars
[forks-shield]: https://img.shields.io/github/forks/marksie1988/home-assistant-config.svg?style=social&label=Forks
[watchers-shield]: https://img.shields.io/github/watchers/marksie1988/home-assistant-config.svg?style=social&label=Watchers

[discord-shield]: https://img.shields.io/discord/330944238910963714.svg
[discord]: https://discord.gg/8JYbyCQ

[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg
[buymeacoffee]: https://www.buymeacoffee.com/marksie1988
