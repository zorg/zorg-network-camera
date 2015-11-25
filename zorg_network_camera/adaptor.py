from zorg.adaptor import Adaptor
import urllib2, urlparse
import os


class Camera(Adaptor):

    def __init__(self, options):
        super(Camera, self).__init__(options)

        self.url = options.get("url", "")
        self.cache_directory = options.get("cache_directory", ".cache")
        self.image_last_modified = None

    def download_image(self):
        """
        Download the image and return the
        local path to the image file.
        """
        split = urlparse.urlsplit(self.url)
        filename = split.path.split("/")[-1]

        # Ensure the directory to store the image cache exists
        if not os.path.exists(self.cache_directory):
            os.makedirs(self.cache_directory)

        filepath = os.path.join(self.cache_directory, filename)

        data = urllib2.urlopen(self.url)
        with open(filepath, "wb") as image:
            image.write(data.read())

        return filepath

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

