**Example 1: 获取投递配置**

获取投递配置

Input: 

```
tccli cls DescribeConsumer --cli-unfold-argument  \
    --TopicId 871710c5-35cd-4d1e-8e79-2fa92c35d612
```

Output: 
```
{
    "Response": {
        "RequestId": "ef9e67c9-8437-477a-8629-06555a3afbbc",
        "Effective": true,
        "Ckafka": {
            "Vip": "127.0.0.1",
            "Vport": "9092",
            "InstanceId": "ckafka-8b4az591",
            "InstanceName": "kafka协议消费监控",
            "TopicId": "topic-jmpmwejg",
            "TopicName": "businesstest000"
        },
        "Content": {
            "EnableTag": true,
            "MetaFields": [
                "__SOURCE__"
            ],
            "TagJsonNotTiled": true,
            "TimestampAccuracy": 0,
            "JsonType": 0
        },
        "NeedContent": true,
        "Compression": 0
    }
}
```

