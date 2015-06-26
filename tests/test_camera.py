from zorg_network_camera.camera import Camera
from unittest import TestCase


class TestCamera(TestCase):

    def setUp(self):
        options = {
            "url": "http://salvius.org/test.jpg"
        }
        self.camera = Camera(options, None)

    def test_get_url(self):
        self.assertEqual(self.camera.get_url(), "http://salvius.org/test.jpg")

    def test_average_brightness(self):
        #brightness = self.camera.average_brightness()
        #self.assertEqual(brightness, 0)
        pass
