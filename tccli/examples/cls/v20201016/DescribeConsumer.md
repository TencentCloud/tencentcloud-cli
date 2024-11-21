**Example 1: 获取投递配置**

获取投递配置

Input: 

```
tccli cls DescribeConsumer --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx",
        "Effective": true,
        "Ckafka": {
            "Vip": "10.123.123.123",
            "Vport": "8088",
            "InstanceId": "xx-xx",
            "InstanceName": "myname",
            "TopicId": "xxxxx-xxx-xxx",
            "TopicName": "name"
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

