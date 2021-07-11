from paho.mqtt import client as mqtt_client
from random import randint
import time
from object_detection_library import detect_moving_objects
from json import dumps




def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def publish(client, topic, filename):

    msg_count = 0

    while True:
        
        for objects_locations in detect_moving_objects(filename):

            time.sleep(1)

            msg = {}
            object_count = 0

            for location in objects_locations:
                msg[f"object number {object_count} location"] = location
                object_count += 1
                time.sleep(1)

            msg = dumps(msg)
            result = client.publish(topic, msg)




if __name__ == '__main__':

    import requests

    # url = 'https://cloclo20.cldmail.ru/public/get/7ZVkDJzzSuQeD7QAHF2CGU7EAuz9MwSg3uAva8QM1UsEPYPSBFzsXMFuYmv7bJtTghsRJv/no/2021-07-08%2010.40.56.MOV'
    # r = requests.get(url)

    # with open('video.MOV', 'wb') as f:
    #     f.write(r.content)
    filename = 'le_video.MOV'

    broker = 'localhost'
    port = 1883
    topic = "object_detection/balls"
    client_id = f'object_detection_sender_{randint(1, 10000)}'

    username = 'sender'
    password = 'password'

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    client.on_connect = on_connect

    client.connect(broker, port)
    client.loop_start()
    publish(client, topic, filename)
