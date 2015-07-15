# Zorg Network Camera

[![Build Status](https://travis-ci.org/zorg-framework/zorg-network-camera.svg?branch=0.0.1)](https://travis-ci.org/zorg-framework/zorg-network-camera)

This module contains device adaptors and drivers that make it possible
to connect network cameras to your robot.

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
