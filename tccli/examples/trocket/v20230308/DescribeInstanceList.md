**Example 1: 查询集群列表**

查询RocketMQ 5.X 集群列表

Input: 

```
tccli trocket DescribeInstanceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
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
                "GroupNum": 10,
                "GroupNumLimit": 500,
                "InstanceId": "rmq-72mo3a9o",
                "InstanceName": "test_instance5x",
                "InstanceStatus": "RUNNING",
                "InstanceType": "EXPERIMENT",
                "MaxMessageDelay": 48,
                "MessageRetention": 72,
                "PayMode": "POSTPAID",
                "Remark": "5.X版本测试集群",
                "ScaledTpsLimit": 0,
                "SkuCode": "experiment_500",
                "TagList": [
                    {
                        "TagKey": "test_tag_key",
                        "TagValue": "test_tag_value"
                    }
                ],
                "TopicNum": 10,
                "TopicNumLimit": 50,
                "TpsLimit": 500,
                "Version": "5.0"
            }
        ],
        "RequestId": "561a34ff-965b-4a2d-852e-973c0b2a6f01",
        "TotalCount": 1
    }
}
```

