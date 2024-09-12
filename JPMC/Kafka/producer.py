from kafka import KafkaProducer

producer = KafkaProducer(value_serializer=str.encode)
prefix = "Python_Producer: "

while True:
    usr_in = input()
    producer.send("topic1", value=prefix + usr_in.lower())
    producer.flush()