from django.utils import unittest
from django.test.client import Client
import time


class HttpTestCase(unittest.TestCase):

    def arduino_get(self):
        arduino = Client()
        return arduino.get('/fan?arduino=1')


    def test_when_arduino_get_fan_it_always_respond_200(self):
        response = self.arduino_get()
        self.assertEquals(response.status_code, 200)


    def test_post_unavailable_fan(self):
        "Client posts valid fan speed (eg: 1) but fan is unavailable => 503"
        self.arduino_get()
        time.sleep(0.15)
        android = Client()
        response = android.post('/fan', {'speed': 1})
        self.assertEqual(response.status_code, 503)


    def test_post_fan_invalid_speed(self):
        "Client posts invalid fan speed (eg: 99) => 400, data = 'Invalid speed'"
        self.arduino_get()
        android = Client()
        response = android.post('/fan', {'speed': 99})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Invalid speed') 


    def test_post_fan_valid_speed(self):
        "Client posts valid fan speed (eg: 2) => 200, data = '1'"
        self.arduino_get()
        android = Client()
        response = android.post('/fan', {'speed': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '2')


    def test_post_twice_fan_valid_speed(self):
        "Client posts valid fan speeds (eg: 2 and 3) => 200, data = '1'"
        self.arduino_get() 
        android = Client()
        response = android.post('/fan', {'speed': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '1')
        response = android.post('/fan', {'speed': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '2')


    def test_get_unavailable_fan(self):
        "Client gets valid fan speed but fan is unavailable => 503"
        android = Client()
        self.arduino_get() 
        time.sleep(0.1)
        response = android.get('/fan')
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.content, 'Fan is not available')


    def test_get_from_arduino(self):
        "Client gets valid fan speed for arduino => 200"
        self.arduino_get() 
        android = Client()
        response = android.post('/fan', {'speed': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '3')

        arduino = Client()
        response = arduino.get('/fan?arduino=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '3')
