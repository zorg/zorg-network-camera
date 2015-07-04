from zorg_network_camera.adaptor import Camera
from zorg_network_camera.feed import Feed
from zorg_network_camera.light_sensor import LightSensor
from unittest import TestCase


class TestFeed(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        connection = Camera(options)
        self.camera = Feed(options, connection)

    def test_get_url(self):
        """
        Test that the url of the image is returned.
        """
        self.assertEqual(
            self.camera.get_url(),
            "http://www.gravatar.com/avatar/0?d=mm"
        )


class TestLightSensor(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        connection = Camera(options)
        self.camera = LightSensor(options, connection)

    def test_get_brightness(self):
        """
        Test that a value for the average
        brightness of the image is returned.
        """
        brightness = self.camera.get_brightness()
        self.assertTrue(brightness > 0)

