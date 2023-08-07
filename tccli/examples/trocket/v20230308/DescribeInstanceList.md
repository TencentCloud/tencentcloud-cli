**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli trocket DescribeInstanceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ExpiryTime": 0,
                "GroupNum": 0,
                "GroupNumLimit": 500,
                "InstanceId": "rmq-4knx4z7p",
                "InstanceName": "tag-test",
                "InstanceStatus": "RUNNING",
                "InstanceType": "EXPERIMENT",
                "MaxMessageDelay": 48,
                "MessageRetention": 72,
                "PayMode": "POSTPAID",
                "Remark": "aabb",
                "ScaledTpsLimit": 0,
                "SkuCode": "experiment_500",
                "TagList": [
                    {
                        "TagKey": "test-key",
                        "TagValue": "tag-value"
                    }
                ],
                "TopicNum": 0,
                "TopicNumLimit": 50,
                "TpsLimit": 500,
                "Version": "5.0"
            },
            {
                "ExpiryTime": 0,
                "GroupNum": 6,
                "GroupNumLimit": 500,
                "InstanceId": "rmq-72mo3a9o",
                "InstanceName": "breatche-test",
                "InstanceStatus": "RUNNING",
                "InstanceType": "EXPERIMENT",
                "MaxMessageDelay": 48,
                "MessageRetention": 24,
                "PayMode": "POSTPAID",
                "Remark": "cddf",
                "ScaledTpsLimit": 0,
                "SkuCode": "experiment_500",
                "TagList": [
                    {
                        "TagKey": "tagkey",
                        "TagValue": "aa"
                    }
                ],
                "TopicNum": 6,
                "TopicNumLimit": 50,
                "TpsLimit": 500,
                "Version": "5.0"
            }
        ],
        "RequestId": "561a34ff-965b-4a2d-852e-973c0b2a6f01",
        "TotalCount": 2
    }
}
```

