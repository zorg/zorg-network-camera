from unittest import TestCase
from zorg_network_camera import Feed
from zorg_network_camera import LightSensor


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
        all_commands_have_methods = True

        for command in feed.commands:
            if command not in dir(feed):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)


class LightSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        sensor = LightSensor(self.options, self.connection)
        all_commands_have_methods = True

        for command in sensor.commands:
            if command not in dir(sensor):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)

