from zorg.driver import Driver
import textract

from Queue import LifoQueue
import threading
import time


class OCR(Driver):

    def __init__(self, options, connection):
        super(OCR, self).__init__(options, connection)

        # The number of read items stored in the queue
        self.queue_size = options.get("queue_size", 10)

        # The frequency of how often to read from the camera (ms)
        self.read_frequency = options.get("read_frequency", 50)

        # A queue of the last text items read by the camera
        self.text_queue = LifoQueue(maxsize=self.queue_size)

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True

        self.commands = [
            "read",
        ]

    def read(self):
        """
        Returns the text from an image at a given url.
        """

        # Only download the image if it has changed
        if not self.connection.has_changed():
            return self.text_queue[0]

        image_path = self.connection.download_image()

        text = textract.process(image_path, encoding='ascii')

        return text

    def is_valid_text(self, text):
        """
        Returns true or false based on if the OCR process has read
        actual words. This is needed to prevent non-words from being
        added to the queue since the ocr process can sometimes return
        values that are not meaningfull.
        """

        # Split the input string at points with any amount of whitespace
        words = text.split()

        # Light weight check to see if a word exists
        for word in text:

            # If the word is a numeric value
            if word.lstrip('-').replace('.','',1).isdigit():
                return True

            # If the word contains only letters with a length from 2 to 20
            if word.isalpha() and (len(word) > 1 or len(word) <= 20):
                return True

        return False

    def run(self):
        """
        Method that runs in the background to check if any text is
        detected in the current image being captured by the camera.
        """
        while True:
            text = self.read()

            # Make sure the text is not already in the queue
            if text != self.text_queue[0]:
                if self.is_valid_text(text):
                    self.text_queue.put(text)

            time.sleep(self.read_frequency)

    def start(self):
        """
        Start the driver. This begins the process of periodically
        checking the camera input for written text.
        """
        self.thread.start()

    def halt(self):
        """
        Stop the driver. This begins the process of periodically
        checking the camera input for written text.
        """
        self.thread.stop()

