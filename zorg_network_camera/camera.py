from zorg.driver import Driver
from urllib2 import urlopen
from PIL import Image, ImageStat
import StringIO


class Camera(Driver):

    def __init__(self, options, connection):
        super(Camera, self).__init__(options, connection)

        self.url = options.get("url", "")

        self.commands = [
            "get_url",
            "average_brightness",
        ]

    def get_url(self):
        """
        Returns the url of the network camera.
        """
        return self.url

    def get_image(self):
        """
        Downloads and returns an image object.
        """
        image_url = urlopen(self.url)
        image_string = StringIO.StringIO(image_url.read())
        return Image.open(image_string)

    def average_brightness(self):
        """
        Return the average brightness of the image.
        """
        converted_image = self.get_image().convert('L')
        statistics = ImageStat.Stat(converted_image)
        return statistics.mean[0]
