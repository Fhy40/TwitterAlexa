__author__ = 'Arjun'

import re
import PyEcho
import time
import twitter
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip': '192.168.2.xx'}, user={'name': 'xxxxxxxxx'})

Blue1 = {
    'which': 1,
    'data': {
        'state': {'on': True, 'hue': 46920, 'bri': 100}
    }
}

Blue2 = {
    'which': 2,
    'data': {
        'state': {'on': True, 'hue': 46920, 'bri': 100}
    }
}

Blue3 = {
    'which': 3,
    'data': {
        'state': {'on': True, 'hue': 46920, 'bri': 100}
    }
}

Red1 = {
    'which': 1,
    'data': {
        'state': {'on': True, 'hue': 65280, 'bri': 100}
    }
}

Red2 = {
    'which': 2,
    'data': {
        'state': {'on': True, 'hue': 65280, 'bri': 100}
    }
}

Red3 = {
    'which': 3,
    'data': {
        'state': {'on': True, 'hue': 65280, 'bri': 100}
    }
}

Green1 = {
    'which': 1,
    'data': {
        'state': {'on': True, 'hue': 25500, 'bri': 100}
    }
}

Green2 = {
    'which': 2,
    'data': {
        'state': {'on': True, 'hue': 25500, 'bri': 100}
    }
}

Green3 = {
    'which': 3,
    'data': {
        'state': {'on': True, 'hue': 25500, 'bri': 100}
    }
}

echo = PyEcho.PyEcho("xxxxxxxxxxx@gmail.com", "xxxxxx")

api = twitter.Api(consumer_key='xxxxxxxx',
                  consumer_secret='xxxxxxxxx',
                  access_token_key='xxxxxxxxxxxxxx',
                  access_token_secret='xxxxxxxxxxxxxxx'
                  )


while True:

    tasks = echo.tasks()

    for task in tasks:

        if (re.split(r'\s', task['text']))[0] == "tweet":
            print "Tweeting"
            s = " "
            status = api.PostUpdate((s.join(re.split(r'\s', task['text']))[5:]))
            echo.deleteTask(task)
        if task['text'] == "blue":
            print "Changing Color to Blue"
            bridge.light.update(Blue1)
            bridge.light.update(Blue2)
            bridge.light.update(Blue3)
            echo.deleteTask(task)
        if task['text'] == "red":
            print "Changing Color to Red"
            bridge.light.update(Red1)
            bridge.light.update(Red2)
            bridge.light.update(Red3)
            echo.deleteTask(task)
        if task['text'] == "green":
            print "Changing Color to Green"
            bridge.light.update(Green1)
            bridge.light.update(Green2)
            bridge.light.update(Green3)
            echo.deleteTask(task)
    time.sleep(10)
    print "Checking Again"

