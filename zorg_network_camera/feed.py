from zorg.driver import Driver


class Feed(Driver):
    """
    This driver provides a method for getting the url of
    the image for a network camera. This may be useful
    when accessing the image through a robot's api.
    """

    def __init__(self, options, connection):
        super(Feed, self).__init__(options, connection)

        self.commands = [
            "get_url",
        ]

    def get_url(self):
        """
        Returns the url of the network camera.
        """
        return self.connection.url
