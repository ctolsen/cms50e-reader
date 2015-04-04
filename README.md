# Data reader for CMS50E Pulse Oximeter

This module reads and outputs data from a Contec CMS50E pulse oximeter.

It has only been tested on Mac OS X Yosemite with Python 3.4. Consider this 
a work in progress.

If you try to upload recorded data from the device, the program will simply
discard the data, but continue working.

Planned features:
- Saving of recorded data
- Live recording and saving
- Web based interface to view pulse waveform data

## Usage

First, [this driver](http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx)
must be installed.

Then:

`python setup.py develop` to install dependencies

`python cms50e.py /path/to/usb-device` to run the program

On the computer used for testing, the usb device was found at
`/dev/cu.SLAB_USBtoUART`. The name of the USB device may be different. 
Running `ls /dev/cu.*` should provide some hints.

Make sure the device has the USB setting on, and is connected to the 
computer. If the program is not outputting any data, simply running 
`cat /path/to/usb-device` can kickstart it.

## Acknowledgements

Written by [Christoffer Torris Olsen](https://github.com/ctolsen/)

Thanks to [Alex Robinson](http://www.tranzoa.net/~alex/blog/?p=371) for
interface documentation.

