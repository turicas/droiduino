#!/usr/bin/env python

import serial
import urllib
import time
import glob


# URL to the Django application
URL = 'http://where-is-hosted-the-django-app/fan?arduino=1'

# Serial port address. /dev/ttyACM* works for Arduino Uno on GNU/Linux.
# Use /dev/ttyUSB* for Duemilanove on GNU/Linux.
SERIAL_PORT = '/dev/ttyACM*'

# Time to wait between two requests (in seconds)
WAIT = 1


class Arduino(object):
    def connect(self, port, baud_rate, timeout=0.1):
        self.arduino = serial.Serial(port, baud_rate, timeout=timeout)
        time.sleep(2)


    def write(self, text):
        self.arduino.write(text)


    def read(self):
        return self.arduino.read()


def get_speed_from_website():
    fan_fp = urllib.urlopen(URL)
    return fan_fp.read()


def log(text):
    print '[%s] %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), text)


last_speed = None
running = True
while running:
    try:
        arduino = Arduino()
        available_ports = glob.glob(SERIAL_PORT)
        if not available_ports:
            log('Arduino not found')
            time.sleep(1)
        else:
            arduino_filename = available_ports[0]
            try:
                arduino.connect(arduino_filename, 9600)
                speed = get_speed_from_website()
                log('Got speed: %s' % speed)
                if last_speed != speed:
                    arduino.write(speed)
                last_speed = speed
                time.sleep(WAIT)
            except serial.serialutil.SerialException:
                log('Serial exception!')
                time.sleep(1)
    except KeyboardInterrupt:
        break
