from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:2181')
for _ in range(7):
  producer.send('topic', b'some_message_bytes')
