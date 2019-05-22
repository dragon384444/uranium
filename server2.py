# Import library mqtt
import paho.mqtt.client as mqtt_client

#agar terkoneksi dengan cloud mqtt lalu menyamakan settingan sesuai user
broker_address = "m11.cloudmqtt.com"
port = 18956
user = "lqbitsna"
password = "T3KrT1UZc0z5"
ambilData = "data test"

def getSub(payload):
	global ambilData
	ambilData = payload
	return ambilData

# Inisiasi sebagai subscriber
sub = mqtt_client.Client("py")
sub.username_pw_set(user, password=password)  # set username and password
sub.connect(broker_address, port=port)  # connect to broker

# Fungsi untuk handle message yang masuk ke subscriber
def handle_message(client, object, msg):
	data	= msg.payload.decode('ascii')
	print("Stock Uranium saat ini: "+data)

# Daftarkan fungsi untuk handle message
sub.on_message = handle_message

# Subscribe ke sebuah topik
sub.subscribe("uranium/sip")
# Loop forever agar subscriber jalan terus
sub.loop_forever()
