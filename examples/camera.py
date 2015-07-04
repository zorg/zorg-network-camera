import time
import zorg

'''
This example creates a robot named CameraBot and
and initializes two cameras named camera_one and
camera_two.

Note: When viewing the api, the url to get the
path to the camera_one image will look like this:
/api/robots/CameraBot/devices/camera_one/commands/get_url
'''

def work(my):
    while True:
        print(my.camera_one.get_url())
        print(my.camera_two.average_brightness())
        time.sleep(1)

robot = zorg.robot({
    "name": "Test",
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
        "camera_two": {
            "connection": "camera",
            "driver": "zorg_network_camera.LightSensor",
            "url": "http://www.gravatar.com/avatar/0000000000000000000?d=mm",
        },
    },
    "work": work,
})

api = zorg.api("zorg.api.Http", {})

robot.start()
api.start()

