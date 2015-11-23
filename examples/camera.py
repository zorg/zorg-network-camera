import time
import zorg

'''
This example creates a robot named CameraBot and
and initializes two devices on the cameras named
camera_one and camera_two.

Note: When viewing the api, the url to get the
path to the camera_one image url will look like this:
/api/robots/CameraBot/devices/camera_one/commands/get_url
'''

def work(my):
    while True:
        print(my.camera_one.get_url())
        print(my.camera_two.get_brightness())
        time.sleep(1)

robot = zorg.robot({
    "name": "CameraBot",
    "connections": {
        "camera": {
            "adaptor": "zorg_network_camera.Camera",
            "url": "http://192.168.10.12/image.jpg",
        },
    },
    "devices": {
        "camera_one": {
            "connection": "camera",
            "driver": "zorg_network_camera.Feed"
        },
        "camera_two": {
            "connection": "camera",
            "driver": "zorg_network_camera.LightSensor"
        },
    },
    "work": work,
})

api = zorg.api("zorg.api.Http", {})

robot.start()
api.start()

