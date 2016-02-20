import time
import zorg

'''
This example creates a robot named CameraBot and
and initializes a device on the camera named ocr.

Note: When viewing the api, the url to get the
path to the camera_one image will look like this:
/api/robots/CameraBot/devices/camera_one/commands/get_url
'''


def work(my):
    while True:
        print(my.ocr.read())
        time.sleep(1)

robot = zorg.robot({
    "name": "CameraBot",
    "connections": {
        "camera": {
            "adaptor": "zorg_network_camera.Camera",
            "url": "http://salvius.org/images/news02.jpg",
        },
    },
    "devices": {
        "ocr": {
            "connection": "camera",
            "driver": "zorg_network_camera.OCR"
        },
    },
    "work": work,
})

api = zorg.api("zorg.api.Http", {})

robot.start()
api.start()
