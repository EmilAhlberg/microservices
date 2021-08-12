from time import sleep
from json import dumps
from kafka import KafkaProducer

import logging
logging.basicConfig(level=logging.DEBUG)

producer = KafkaProducer(
    bootstrap_servers=['0.0.0.0:9092'],
    api_version=(2,7,0),
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send('topic_test', value=data)
    sleep(0.5)
