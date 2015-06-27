from zorg_network_camera.camera import Camera
from unittest import TestCase


class TestCamera(TestCase):

    def setUp(self):
        options = {
            "url": "http://www.gravatar.com/avatar/0?d=mm"
        }
        self.camera = Camera(options, None)

    def test_get_url(self):
        """
        Test that the url of the image is returned.
        """
        self.assertEqual(
            self.camera.get_url(),
            "http://www.gravatar.com/avatar/0?d=mm"
        )

    def test_get_image(self):
        """
        Test that the image file can be downloaded.
        """
        import os
        image_path = self.camera.download_image()
        self.assertTrue(os.path.exists(image_path))

        # Clean up after testing
        os.remove(image_path)

    def test_has_changed(self):
        """
        Test that False is returned when the
        image is checked for the first time.
        """
        response = self.camera.has_changed()
        self.assertTrue(response)
        self.assertFalse(self.camera.image_last_modified is None)

    def test_has_changed_modified(self):
        """
        Test that True is returned when the
        last modified header changes.
        """
        pass

    def test_has_changed_not_modified(self):
        """
        Test that False is returned when the
        last modified header has not changed.
        """
        pass

    def test_has_changed_no_modified_header(self):
        """
        Test that True is returned when the
        last modified header is not present.
        """
        pass

    def test_average_brightness(self):
        """
        Test that a value for the average
        brightness of the image is returned.
        """
        brightness = self.camera.average_brightness()
        self.assertTrue(brightness > 0)

