from unittest import TestCase
from zorg_network_camera import Feed
from zorg_network_camera import LightSensor
from zorg_network_camera import OCR


class SmokeTestCase(TestCase):

    def setUp(self):
        self.connection = None
        self.options = {}


class FeedSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        feed = Feed(self.options, self.connection)

        for command in feed.commands:
            self.assertIn(command, dir(feed))


class LightSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        sensor = LightSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class OCRSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        sensor = OCR(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))

