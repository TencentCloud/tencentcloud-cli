**Example 1: 获取投递配置**

获取投递配置

Input: 

```
tccli cls DescribeConsumer --cli-unfold-argument  \
    --TopicId bowwwang-json-test-1254139626
```

Output: 
```
{
    "Response": {
        "Ckafka": {
            "InstanceId": "ckafka-8j4ro593",
            "InstanceName": "kafka协议消费***(******测试******",
            "TopicId": "topic-78joudry",
            "TopicName": "ri****st",
            "Vip": "10.***.**",
            "Vport": "90**"
        },
        "Compression": 0,
        "Content": {
            "AutoConvertNumber": false,
            "EnableTag": true,
            "JsonType": 1,
            "MetaFields": [
                "__SOURCE__"
            ],
            "TagJsonNotTiled": false,
            "TimestampAccuracy": 2
        },
        "CreateTime": 1729504453000,
        "Effective": false,
        "ExternalId": "",
        "NeedContent": true,
        "RoleArn": "",
        "TaskStatus": 0,
        "RequestId": "530f50db-ae27-4438-8d6b-bca035faebc9"
    }
}
```

