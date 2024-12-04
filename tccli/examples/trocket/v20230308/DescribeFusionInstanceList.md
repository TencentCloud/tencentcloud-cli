**Example 1: 获取全量集群列表**



Input: 

```
tccli trocket DescribeFusionInstanceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Data": [
            {
                "InstanceId": "rmq-72mo3a9o",
                "InstanceName": "test_instance5x",
                "Version": "5.0",
                "InstanceType": "EXPERIMENT",
                "InstanceStatus": "RUNNING",
                "TopicNumLimit": 52,
                "GroupNumLimit": 520,
                "PayMode": "PREPAID",
                "ExpiryTime": 1731830193435,
                "Remark": "5.X 版本测试集群",
                "TopicNum": 3,
                "GroupNum": 10,
                "TagList": [
                    {
                        "TagKey": "test_tag",
                        "TagValue": "test_tag_key"
                    }
                ],
                "SkuCode": "experiment_500",
                "TpsLimit": 500,
                "ScaledTpsLimit": 0,
                "MessageRetention": 72,
                "MaxMessageDelay": 168,
                "RenewFlag": 1,
                "InstanceItemExtraInfo": {
                    "IsVip": false,
                    "VipInstanceStatus": 0,
                    "MaxBandWidth": 0,
                    "SpecName": "",
                    "NodeCount": 0,
                    "MaxStorage": 0,
                    "MaxRetention": 0,
                    "MinRetention": 0,
                    "InstanceStatus": 0
                },
                "DestroyTime": 0
            },
            {
                "InstanceId": "rocketmq-5kze4gr222mx",
                "InstanceName": "test_instance4x",
                "Version": "4",
                "InstanceType": "BASIC",
                "InstanceStatus": "RUNNING",
                "TopicNumLimit": 400,
                "GroupNumLimit": 4000,
                "PayMode": "PREPAID",
                "ExpiryTime": 1730710586538,
                "Remark": "4.X 版本测试集群",
                "TopicNum": 1,
                "GroupNum": 1,
                "TagList": [
                    {
                        "TagKey": "test_tag",
                        "TagValue": "test_tag_key"
                    }
                ],
                "SkuCode": "",
                "TpsLimit": 8000,
                "ScaledTpsLimit": 0,
                "MessageRetention": 72,
                "MaxMessageDelay": 0,
                "RenewFlag": 1,
                "DestroyTime": 0,
                "InstanceItemExtraInfo": {
                    "IsVip": true,
                    "InstanceStatus": 1,
                    "VipInstanceStatus": 1,
                    "MaxBandWidth": 80,
                    "NodeCount": 2,
                    "MaxStorage": 200,
                    "SpecName": "rocket-vip-basic-0",
                    "MaxRetention": 168,
                    "MinRetention": 24
                }
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

