# NO LONGER COMPATIBLE
Hi folks, unfortunately it seems the Parsec team have made a lot of changes to Parsec recently that are good, but break compatability with this plugin for the time being. If and when Parsec becomes available for the Pi 4, I'll be able to resume development on this plugin, but for the time being this is defunct. Please feel free to fork and continue if you can!

# Parsec Launcher for OSMC
Parsec is a game streaming application used to play video games remotely across a conntected network from a system in the cloud to your home computer. OSMC (short for Open Source Media Center) is a Linux distribution based on Debian that brings Kodi to a variety of devices. This addon brings the two together to create a seamless experience.

![Add-on Configuration](https://i.imgur.com/qm2vHi9.jpg)
![Add-on Settings](https://i.imgur.com/63NWEMi.jpg)

## Features
* Launch Parsec from Kodi on your Raspberry Pi running OSMC.
* Easily configure your Parsec connection from within the addon configuration menu.
* Automatically exit back into Kodi after your Parsec session has ended.
* Seamlessly launch directly into your Parsec host without having to enter login or host selection information by enabling Headless Client Mode.

## Requirements
* Raspberry Pi Device
* OSMC installed on your device - [Download & Installation Instructions](https://osmc.tv/download/).
* Parsec installed on your device - [Download & Installation Instructions](https://support.parsecgaming.com/hc/en-us/articles/115002699012-Setting-Up-On-Raspberry-Pi-Raspbian-).
* Parsec installed on a host machine or cloud instance to connect to.
* USB keyboard (wired or wireless)

## Installation
* Download production package **script.parsec.zip** [here](http://dev.grantgarrison.com/projects/script.parsec.zip).
* Follow the addon installation instructions **HOW-TO:Install add-ons from zip files** [here](https://kodi.wiki/view/HOW-TO:Install_add-ons_from_zip_files).

## Configuration
* You can find the configuration settings for this addon by opening the context menu with the addon selected.
* You can open the context menu by doing the following actions:
  * Long pressing the OK/enter key on your remote.
  * Pressing letter C on a keyboard.
  * Right-clicking with the mouse.

## First Time Setup
1. You can find this addon in the *Programs* menu of OSMC's home menu. *(Similar location in Kodi)*
1. On first launch, Parsec will ask you to enter your username and password.<br /> 
You'll need to connect a USB keyboard in order to enter this in.
1. Parsec will then ask you if you want to save this information.<br />
I reccomend doing so so that you won't have to do so again each time you launch Parsec from the addon.

## Exiting Parsec
* In order to exit Parsec back into Kodi on your Raspberry Pi running OSMC, you'll need to enter the following command on your keyboard.
  * Ctrl + Alt + ~

## Future Development
* If you're a savvy developer, please feel free to fork this project. I'd love to expand this to LibreELEC and Raspbian running Kodi, but unfortunately I just don't have time to learn how. OSMC's environment and dependencies made putting this together much easier than on other platforms.
* Once OSMC and Parsec are released on Raspberry Pi 4, I'll be looking to open this project back up, update the branding to Parsec's new brand package and reconsider the feature set as Parsec has evolved quite a bit since the creationg of this plugin and things that used to be set on the client side aren't anymore. (Correct me if I'm wrong on that.)

http://dev.grantgarrison.com
