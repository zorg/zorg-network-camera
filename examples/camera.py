import time
import zorg

'''
This example creates a robot named Test and
and initializes a camera named camera_one.
The url to get the path to the camera image
will look like this:
/api/robots/Test/devices/camera_one/commands/get_url
'''

robot = zorg.robot({
    "name": "Test",
    "connections": {
        "edison": {
            "adaptor": "zorg_edison.Edison",
        },
    },
    "devices": {
        "camera_one": {
            "connection": "edison",
            "driver": "zorg_network_camera.Camera",
            "url": "http://192.168.10.12/image.jpg",
        },
    },
    "work": None,
})

api = zorg.api("zorg.api.Http", {})

robot.start()
api.start()

