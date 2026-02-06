**Example 1: 获取投递规则**



Input: 

```
tccli cls DescribeConsumers --cli-unfold-argument  \
    --Filters.0.Key ConsumerId \
    --Filters.0.Values xxxx-xxx-xxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Consumers": [
            {
                "ConsumerId": "66f5808c-4a55-11eb-b378-0242ac131112",
                "TopicId": "57f5808c-4a55-11eb-b378-0242ac130002",
                "Effective": true,
                "Ckafka": {
                    "Vip": "10.111.1.123",
                    "Vport": "8888",
                    "InstanceId": "ckafka-8j111111",
                    "InstanceName": "myname",
                    "TopicId": "topic-icjnxxx",
                    "TopicName": "125xxx-qwerty5-355a-492a-9dba-790271f5da27"
                },
                "NeedContent": true,
                "Content": {
                    "EnableTag": true,
                    "MetaFields": [
                        "abc"
                    ],
                    "TagJsonNotTiled": true,
                    "TimestampAccuracy": 0,
                    "JsonType": 0
                },
                "Compression": 0,
                "CreateTime": 1662034960,
                "RoleArn": "qcs::cam::uin/${uin}:roleName/xxxtest",
                "ExternalId": "external_id_demo",
                "TaskStatus": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "1235808c-4a55-11eb-b378-0242ac133212"
    }
}
```

