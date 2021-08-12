from json import loads
from time import sleep
from kafka import KafkaConsumer
consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['0.0.0.0:9092'],
    api_version=(2,7,0),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(2)
