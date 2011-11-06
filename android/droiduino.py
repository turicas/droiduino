# -*- coding: utf-8 -*-
import android
import httplib
import json
import urllib

SERVER = "pybr7.cursodearduino.com.br"
FAN_VIEW = 'file:///sdcard/sl4a/scripts/html/fan.html'


def http_get():
    connection = httplib.HTTPConnection(SERVER)
    connection.request("GET", "/fan")
    response = connection.getresponse()
    connection.close()
    return response

class FanController(object):

    def __init__(self, speed=0):
        self.droid = android.Android()
        self.speed = speed
        #self.handlers = {"getFanSpeed": self.get_speed,
        #                 "setFanSpeed": self.set_speed}
        self.handlers = {"mudar_velocidade": self.set_speed,
                         "atualizar_velocidade": self.get_speed,}

    def exit(self, data=None):
        exit()

    def start(self):
        self.droid.webViewShow(FAN_VIEW)

        action = ""
        while action != "EXIT":
            event_data = self.droid.eventWaitFor("PYTHON").result["data"]
            # unpack the event data and perform action(if available).
            properties = json.loads(event_data)
            action = properties["action"]
            if action in self.handlers:
                self.handlers[action](properties["data"])

    def get_speed(self, data=None):
        # get the new speed from the server
        response = http_get()
        # analyse the response
        if response.status == 200:
            new_speed = response.read()
            self.speed = int(new_speed)
            #self.update_view_speed()
            msg = 'Successfuly retrieved fan speed. It is %s' % new_speed
        elif response.status == 503:
            msg = 'Service unavailable'
        else:
            msg = 'Oops, a %d occured' % status

        self.alert(msg)
        self.droid.makeToast(msg)
        self.droid.ttsSpeak(msg)
        self.update_view_speed()

    def set_speed(self, speed):
        # post new speed to server
        if speed == '':
            speed = '0'
        params = urllib.urlencode({'speed': int(speed)})
        connection = httplib.HTTPConnection(SERVER)
        connection.request("POST", "/fan/", params)
        response = connection.getresponse()

        # analyse the response 
        if response.status == 200:
            msg = 'Speed set to %s' % speed
            self.speed = speed
        elif response.status == 503:
            msg = 'Service unavailable'
        else:
            msg = 'Oops, a %d error occured' % response.status
        connection.close()

        self.alert(msg)
        self.droid.makeToast(msg)
        self.droid.ttsSpeak(msg)
        #self.update_view_speed()

        # alert success or failure
        self.alert(msg)

    def update_view_speed(self):
        self.droid.eventPost("fanSpeedChanged", json.dumps(int(self.speed)))

    def alert(self, msg):
        print msg

if __name__ == '__main__':
    fan = FanController()
    fan.start()


