from zorg_network_camera.adaptor import Camera
from zorg_network_camera.feed import Feed
from zorg_network_camera.light_sensor import LightSensor
from zorg_network_camera.ocr import OCR
from unittest import TestCase
from mock import MagicMock
import os
import shutil


class TestFeed(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        self.connection = Camera(options)
        self.camera = Feed(options, self.connection)

    def test_get_url(self):
        """
        Test that the url of the image is returned.
        """
        self.assertEqual(
            self.camera.get_url(),
            "http://www.gravatar.com/avatar/0?d=mm"
        )

    def tearDown(self):
        """
        Clean up by removing the test image that was downloaded.
        """
        if os.path.exists(self.connection.cache_directory):
            shutil.rmtree(self.connection.cache_directory)


class TestLightSensor(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        self.connection = Camera(options)
        self.camera = LightSensor(options, self.connection)

    def test_get_brightness(self):
        """
        Test that a value for the average
        brightness of the image is returned.
        """
        brightness = self.camera.get_brightness()
        self.assertTrue(brightness > 0)

    def tearDown(self):
        """
        Clean up by removing the test image that was downloaded.
        """
        if os.path.exists(self.connection.cache_directory):
            shutil.rmtree(self.connection.cache_directory)


class TestOCR(TestCase):

    def setUp(self):
        options = {
            "url": "http://salvius.org/images/news02.jpg"
        }
        connection = Camera(options)

        # Mock the the image returned by the download method
        connection.download_image = MagicMock(return_value="tests/news.jpg")

        self.ocr = OCR(options, connection)

    def test_ocr(self):
        text = self.ocr.read()
        self.assertIn("ROBOT BUILDER from page 1", text)

    def test_invalid_text(self):
        """
        Test that a string containing no
        words returns false.
        """
        # Mock the read method to return a non-word string.
        self.ocr.read = MagicMock(
            return_value="<()> ~$ %^ H4 fuha9 &&.0 --@-- Qs!"
        )

        text_detected = self.ocr.text_visible()
        self.assertFalse(text_detected)

    def test_valid_text(self):
        """
        Test that a string containing words returns true.
        """
        # Mock the read method to return a non-word string.
        self.ocr.read = MagicMock(return_value="Scientific American volume 307")

        text_detected = self.ocr.text_visible()
        self.assertTrue(text_detected)

