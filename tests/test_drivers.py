from zorg_network_camera.adaptor import Camera
from zorg_network_camera.feed import Feed
from zorg_network_camera.light_sensor import LightSensor
from zorg_network_camera.ocr import OCR
from unittest import TestCase
from mock import MagicMock


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


class TestOCR(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        connection = Camera(options)
        self.ocr = OCR(options, connection)

    def test_invalid_text(self):
        """
        Test that a string containing no
        words returns false.
        """
        options = {
            "url": "http://salvius.org/images/news02.jpg"
        }
        connection = Camera(options)
        ocr = OCR(options, connection)

        # Mock the read method to return a non-word string.
        ocr.read = MagicMock(return_value="<()> ~$ %^ H4 fuha9 &&.0 --@-- Qs!")

        text_detected = ocr.text_visible()
        self.assertFalse(text_detected)

    def test_valid_text(self):
        """
        Test that a string containing words returns true.
        """
        options = {
            "url": "http://salvius.org/images/news02.jpg"
        }
        connection = Camera(options)
        ocr = OCR(options, connection)

        # Mock the read method to return a non-word string.
        ocr.read = MagicMock(return_value="Scientific American volume 307")

        text_detected = ocr.text_visible()
        self.assertTrue(text_detected)

