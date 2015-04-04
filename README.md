# Data reader for CMS50E Pulse Oximeter

This module reads and outputs data from a Contec CMS50E pulse oximeter.

It has only been tested on Mac OS X Yosemite. Consider this a work in progress.

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

`python cms50e.py /dev/cu.SLAB_USBtoUART`

The name of the USB device may be different. Running `ls /dev/cu.*` should
provide some hints.

## Acknowledgements

Written by Christoffer Torris Olsen <chris@torristory.com>.

Thanks to [Alex Robinson](http://www.tranzoa.net/~alex/blog/?p=371) for
interface documentation.

