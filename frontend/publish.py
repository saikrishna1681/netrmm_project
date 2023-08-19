import paho.mqtt.client as mqtt

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
    else:
        print('Bad connection. Code:', rc)


def on_publish(mqtt_client, userdata, msg):
    print( userdata,msg,'published')


client = mqtt.Client()
client.connect(host="localhost", port=1883, keepalive=60)

client.on_connect = on_connect
client.on_publish = on_publish
