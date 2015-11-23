from unittest import TestCase
from zorg import robot


class TestSerialize(TestCase):

    def test_serialize_connections(self):
        bot = robot({
            "name": "TestRobot1",
            "connections": {
                "camera": {
                    "adaptor": "zorg_network_camera.Camera",
                },
            },
            "devices": {
                "camera_one": {
                    "connection": "camera",
                    "driver": "zorg_network_camera.Feed",
                    "url": "http://192.168.10.12/image.jpg",
                },
            },
            "work": None,
        })

        self.assertTrue(len(bot.serialize_connections()))

    def test_serialize_devices(self):
        bot = robot({
            "name": "TestRobot2",
            "connections": {
                "camera": {
                    "adaptor": "zorg_network_camera.Camera",
                },
            },
            "devices": {
                "camera_one": {
                    "connection": "camera",
                    "driver": "zorg_network_camera.Feed",
                    "url": "http://192.168.10.12/image.jpg",
                },
            },
            "work": None,
        })

        self.assertTrue(len(bot.serialize_devices()))
