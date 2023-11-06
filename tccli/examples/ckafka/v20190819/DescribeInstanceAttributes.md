**Example 1: 获取实例属性**



Input: 

```
tccli ckafka DescribeInstanceAttributes --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceId": "abc",
            "InstanceName": "abc",
            "VipList": [
                {
                    "Vip": "abc",
                    "Vport": "abc"
                }
            ],
            "Vip": "abc",
            "Vport": "abc",
            "Status": 0,
            "Bandwidth": 0,
            "DiskSize": 0,
            "ZoneId": 0,
            "VpcId": "abc",
            "SubnetId": "abc",
            "Healthy": 0,
            "HealthyMessage": "abc",
            "CreateTime": 1,
            "MsgRetentionTime": 0,
            "Config": {
                "AutoCreateTopicsEnable": true,
                "DefaultNumPartitions": 0,
                "DefaultReplicationFactor": 0
            },
            "RemainderPartitions": 0,
            "RemainderTopics": 0,
            "CreatedPartitions": 0,
            "CreatedTopics": 0,
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "ExpireTime": 1,
            "ZoneIds": [
                0
            ],
            "Version": "abc",
            "MaxGroupNum": 0,
            "Cvm": 0,
            "InstanceType": "abc",
            "Features": [
                "abc"
            ],
            "RetentionTimeConfig": {
                "Enable": 0,
                "DiskQuotaPercentage": 0,
                "StepForwardPercentage": 0,
                "BottomRetention": 0
            },
            "MaxConnection": 1,
            "PublicNetwork": 0,
            "DeleteRouteTimestamp": "abc",
            "RemainingPartitions": 0,
            "RemainingTopics": 0,
            "DynamicDiskConfig": {
                "Enable": 0,
                "StepForwardPercentage": 0,
                "DiskQuotaPercentage": 0,
                "MaxDiskSpace": 0
            },
            "InstanceChargeType": "abc"
        },
        "RequestId": "abc"
    }
}
```

