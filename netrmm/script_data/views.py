import paho.mqtt.client as mqtt
import json
from . import mqtt_handler

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully mqtt')
    else:
        print('Bad connection. Code:', rc)


def on_subscribe(mqtt_client, userdata ,msg, next):
    print("subscribed")
    #print(userdata, msg, next)


def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic}')
    topic=msg.topic
    payload=json.loads(msg.payload)

    if topic=="save_script":
        mqtt_handler.save_script(request=payload)
    elif topic== "new_script":
        mqtt_handler.new_script(request=payload)
    elif topic=="save_log":
        mqtt_handler.save_log(request=payload)
    elif "delete_script/" in topic:
        id = topic.split("/")[1]
        id = int(id)
        print("*"*100,id)
        mqtt_handler.delete_script(id)
    else:
        print("invalid request", payload)
        

client = mqtt.Client()
client.connect(host="localhost", port=1883, keepalive=60)

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.subscribe("testting")
client.subscribe("save_script")
client.subscribe("new_script")
client.subscribe("save_log")
client.subscribe("delete_script/#")

client.loop_start()