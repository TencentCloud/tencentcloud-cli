**Example 1: 获取投递配置**



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
            "Vport": "8888",
            "InstanceId": "xxxxx",
            "InstanceName": "myname",
            "TopicId": "xxxxx",
            "TopicName": "xxxxx"
        },
        "Content": {
            "EnableTag": true,
            "MetaFields": [
                "__SOURCE__"
            ]
        },
        "NeedContent": true,
        "Compression": 0
    }
}
```

