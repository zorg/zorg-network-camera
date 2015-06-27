from zorg.driver import Driver
from PIL import Image, ImageStat
import urllib2, urlparse


class LightSensor(Driver):
    """
    This driver makes it possible to use a camera
    as a light sensor by analyzing the lighting
    levels of the image.
    """

    def __init__(self, options, connection):
        super(LightSensor, self).__init__(options, connection)

        self.url = options.get("url", "")
        self.image_last_modified = None

        self.image_brightness = 0

        self.commands = [
            "average_brightness",
        ]

    def download_image(self):
        """
        Download the image and return the
        local path to the image file.
        """
        split = urlparse.urlsplit(self.url)
        filename = split.path.split("/")[-1]

        data = urllib2.urlopen(self.url)
        with open(filename, "wb") as image:
            image.write(data.read())

        return filename

    def has_changed(self):
        """
        Method to check if an image has changed
        since it was last downloaded. By making
        a head request, this check can be done
        quicker that downloading and processing
        the whole file.
        """
        request = urllib2.Request(self.url)
        request.get_method = lambda : 'HEAD'

        response = urllib2.urlopen(request)
        information = response.info()

        if 'Last-Modified' in information:
            last_modified = information['Last-Modified']

            # Return False if the image has not been modified
            if last_modified == self.image_last_modified:
                return False

        self.image_last_modified = last_modified

        # Return True if the image has been modified
        # or if the image has no last-modified header
        return True

    def average_brightness(self):
        """
        Return the average brightness of the image.
        """
        # Only download the image if it has changed
        if not self.has_changed():
            return self.image_brightness

        image_path = self.download_image()

        converted_image = Image.open(image_path).convert('L')
        statistics = ImageStat.Stat(converted_image)

        self.image_brightness = statistics.mean[0]
        return self.image_brightness

