# Kafka Producer

Start Zookeeper:

```
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```

Start Kafka:

```
kafka-server-start /usr/local/etc/kafka/server.properties
```

_NOTE_: DO NOT STOP ZOOKEEPER UNTIL KAFKA IS STOPPED

Create a topic on Kafka server:

```
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test-topic
```

List topics on the Kafka server:

```
kafka-topics --list --zookeeper localhost:2181
```

Start producer console:

```
kafka-console-producer --broker-list localhost:9092 --topic test-topic
```

Start consumer console:

```
kafka-console-consumer --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```

Stop docker:

```
docker-machine stop default
```
