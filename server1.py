# Import library mqtt
import paho.mqtt.client as mqtt_client

#agar terkoneksi dengan cloud mqtt lalu menyamakan settingan sesuai user
broker_address = "m11.cloudmqtt.com"
port = 18956
user = "lqbitsna"
password = "T3KrT1UZc0z5"
tempData = 0 #untuk penyimpanan data sementara

# Inisiasi sebagai subscriber
sub = mqtt_client.Client("py-sub")
sub.username_pw_set(user, password=password)  # set username and password
sub.connect(broker_address, port=port)  # connect to broker

# Fungsi untuk handle message yang masuk ke subscriber
def handle_message(client, object, msg):
    global tempData
    data	= int(msg.payload.decode('ascii'))
    print(data)
    if(data < 0):
        tempData = tempData + data
    if(data >= 0):
        tempData = tempData + data

    print(tempData)
    sub.publish("uranium/sip", tempData);

# Daftarkan fungsi untuk handle message
sub.on_message = handle_message

# Subscribe ke sebuah topik
sub.subscribe("python/test")
# Loop forever agar subscriber jalan terus
sub.loop_forever()
