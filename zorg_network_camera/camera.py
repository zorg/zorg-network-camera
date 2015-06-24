from zorg.driver import Driver


class Camera(Driver):

    def __init__(self, options, connection):
        super(Camera, self).__init__(options, connection)

        self.url = options.get("url", "")

        self.commands = [
            "get_url",
        ]

    def get_url(self):
        """
        Returns the url of the network camera.
        """
        return self.url
