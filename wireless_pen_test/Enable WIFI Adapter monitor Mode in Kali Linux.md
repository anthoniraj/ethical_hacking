# Enable WIFI ADAPTER Monitor Mode in Kali Linux
- Author: Anthoniraj Amalanathan

## Connect the WIFI adapter and add it in VirtualBox USB Settings
 - TP-Link TL-WN725N 150Mbps Wireless N Nano USB Adapter 
 - https://www.amazon.in/gp/product/B008IFXQFU

## Check the Adapter Chippet
```bash
lsusb
Bus 001 Device 002: ID 2357:0109 TP-Link TL-WN823N v2/v3 [Realtek RTL8192EU]
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 002: ID 80ee:0021 VirtualBox USB Tablet
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
```

## Find Appropriate Driver for Realtek RTL8192EU from GitHub
- https://github.com/clnhub/rtl8192eu-linux

## Install the dependencies 
- `sudo apt install linux-headers-generic build-essential dkms git`

## Clone the Driver
- `clone https://github.com/clnhub/rtl8192eu-linux.git`

## Configure the Architecture and Monitor Mode
- Open MakeFile in Text Editor or Nano
- If you're using a different architecture than x86, the  
	- set (MakeFile) CONFIG_PLATFORM_I386_PC = n 
	- set your architecture CONFIG_PLATFORM_ARM_AARCH64 = y for 64-bit.
- Set CONFIG_WIFI_MONITOR = y for enabling monitor mode

## Install the driver
- ` sudo ./install_wifi.sh`
- Reboot Kali linux

## To Enable Monitor Mode
- sudo ifconfig wlan0 down
- sudo iwconfig wlan0 mode monitor
- sudo ifconfig wlan0 up

## To Disable monitor mode
- sudo ifconfig wlan0 down
- sudo iwconfig wlan0 mode managed
- sudo ifconfig wlan0 up