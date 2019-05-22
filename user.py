# inisialisasi library
import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

#agar terkoneksi dengan cloud mqtt lalu menyamakan settingan sesuai user
Connected = False   #global variable for the state of the connection
broker_address = "m11.cloudmqtt.com"
port = 18956
user = "lqbitsna"
password = "T3KrT1UZc0z5"

#menyetting user sebagai client
client = mqttClient.Client("python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

#perulangan untuk menunggu koneksi
while Connected != True:    #Wait for connection
    time.sleep(0.1)

#perulangan untuk menginput data
try:
    while True:
        value = input('Masukan jumlah uranium saat ini(gram): ')
        client.publish("python/test",value)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()