## pip install kafka-python

from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name = "testevent"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode("utf-8"))
for e in range(10):
	data = ('number:', e)
	print(data)
	producer.send(topic_name, value=data)
	sleep(5)
	
