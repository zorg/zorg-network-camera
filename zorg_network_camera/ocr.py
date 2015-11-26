from zorg.driver import Driver
from PIL import Image
import pytesseract


class OCR(Driver):

    def __init__(self, options, connection):
        super(OCR, self).__init__(options, connection)

        # An attribute to hold the last text item read by the camera
        self.text_cache = ""

        self.commands = [
            "read",
            "text_visible"
        ]

    def read(self):
        """
        Returns the text from an image at a given url.
        """

        # Only download the image if it has changed
        if self.connection.has_changed():
            image_path = self.connection.download_image()
            image = Image.open(image_path)
            self.text_cache = pytesseract.image_to_string(image)
            image.close()

        return self.text_cache

    def text_visible(self):
        """
        Returns true or false based on if the OCR process has read
        actual words. This is needed to prevent non-words from being
        added to the queue since the ocr process can sometimes return
        values that are not meaningfull.
        """

        # Split the input string at points with any amount of whitespace
        words = self.read().split()

        # Light weight check to see if a word exists
        for word in words:

            # If the word is a numeric value
            if word.lstrip('-').replace('.','',1).isdigit():
                return True

            # If the word contains only letters with a length from 2 to 20
            if word.isalpha() and (len(word) > 1 or len(word) <= 20):
                return True

        return False

