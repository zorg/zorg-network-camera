# Zorg Network Camera

[![PYPI](https://img.shields.io/pypi/v/zorg-network-camera.svg)](https://pypi.python.org/pypi/zorg-network-camera/)
[![Build Status](https://travis-ci.org/zorg/zorg-network-camera.svg?branch=0.0.1)](https://travis-ci.org/zorg/zorg-network-camera)
[![Coverage Status](https://coveralls.io/repos/github/zorg/zorg-network-camera/badge.svg?branch=master)](https://coveralls.io/github/zorg/zorg-network-camera?branch=master)

This module contains device adaptors and drivers that make it possible
to connect network cameras to your robot.

## Installation

```
pip install zorg-network-camera
```

## Network Camera Adaptor

This module's network camera adaptor handles the basic functions of
retrieving images from the remote camera when necessary. Because this
module is intended to run on devices such as the Intel Edison or the
Raspberry Pi, the adaptor has been designed with additional features
for efficiency. Mainly, if an images are cached until the image from
the remote camera has been updated. This ensures that an image will
not be unnecessarily downloaded onto the device.

### Camera Feed Driver

The `Feed` module provides a driver for accessing the url to of the
remote camera's image. This is a convenience method intended to be
used to load the image into your application.

### Light Sensor Driver

The `LightSensor` module allows you to use the camera as a light sensor.
This driver provides the ability to get the average lighting level from
the camera.

### OCR Driver

Optical character recognition (OCR) is the process of programmatically
converting images of typed, handwritten or printed text into machine-encoded
text. The `OCR` driver module provided in this package provides a utility that
makes it possible for your robot to process written text that it sees.

The OCR driver achieves the process of extracting text from an image through
the use of the open source [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
module. Tesseract is an optical character recognition engine origionally
developed by Hewlett-Packard. Development of Tesseract has been
[sponsored by Google since 2006](http://googlecode.blogspot.com/2006/08/announcing-tesseract-ocr.html).

