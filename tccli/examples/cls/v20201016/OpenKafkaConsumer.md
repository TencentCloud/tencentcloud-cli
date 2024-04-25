**Example 1: 打开Kafka协议消费功能**

打开Kafka协议消费功能

Input: 

```
tccli cls OpenKafkaConsumer --cli-unfold-argument  \
    --FromTopicId a5ce0c9c-0690-44a5-bc79-5f2190626bd0 \
    --Compression 0
```

Output: 
```
{
    "Response": {
        "TopicID": "out-a5ce0c9c-0690-44a5-bc79-5f2190626bd0",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

