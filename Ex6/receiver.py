from paho.mqtt import client as mqtt_client
from random import randint




def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):

    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")




if __name__ == '__main__':

    broker = 'localhost'
    port = 1883
    topic = "object_detection/balls"
    client_id = f'object_detection_t_{randint(1, 10000)}'

    username = 'receiver'
    password = 'password'

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    client.subscribe(topic)
    client.loop_forever()
