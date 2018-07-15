# OSMC/Kodi Addon: Parsec Launcher
Parsec is a game streaming application used to play video games remotely across a conntected network from a system in the cloud to your home computer. OSMC (short for Open Source Media Center) is a Linux distribution based on Debian that brings Kodi to a variety of devices. This addon brings the two together to create a seamless experience.

## Features
* Launch Parsec from OSMC/Kodi on your Raspberry Pi.
* Easily configure your Parsec connection from within the addon configuration menu.
* Automatically exit back into OSMC/Kodi after your Parsec session has ended.
* Seamlessly launch directly into your Parsec host without having to enter login or host selection information by enabling Headless Client Mode.

## Requirements
* Raspberry Pi Device
* OSMC installed on your device - [Download & Installation Instructions](https://osmc.tv/download/).
* Parsec installed on your device - [Download & Installation Instructions](https://support.parsecgaming.com/hc/en-us/articles/115002699012-Setting-Up-On-Raspberry-Pi-Raspbian-).
* Parsec installed on a host machine or cloud instance to connect to.
* USB keyboard (wired or wireless)

## Installation
* Download production package [here](http://dev.grantgarrison.com/projects/script.parsec.zip).
* Follow the addon installation instructions [here](https://kodi.wiki/view/HOW-TO:Install_add-ons_from_zip_files).

## First Time Setup
1. You can find this addon in the *Programs* menu of OSMC's home menu. *(Similar location in Kodi)*
1. On first launch, Parsec will ask you to enter your username and password.<br /> 
You'll need to connect a USB keyboard in order to enter this in.
1. Parsec will then ask you if you want to save this information.<br />
I reccomend doing so so that you won't have to do so again each time you launch Parsec from the addon addon.

## Configuration
* You can find the configuration settings for this addon by opening the context menu with the addon selected.
* You can open the context menu by doing the following actions:
  * Long pressing the OK/enter key on your remote.
  * Pressing letter C on a keyboard.
  * Right-clicking with the mouse.

## Known Bugs
* Not sure if all client side configurations are working properly. Server side resolution hasn't appered to work but might be due to a limitation in Parsec itself.

## Future Development
* Raspbian + Kodi functionality currently being tested.
* Other platforms being considered.
<br /><br />http://dev.grantgarrison.com
