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
            "MsgRetentionTime": 1440,
            "DeleteRouteTimestamp": "xx",
            "Version": "xx",
            "Config": {
                "DefaultNumPartitions": 0,
                "AutoCreateTopicsEnable": true,
                "DefaultReplicationFactor": 2
            },
            "RemainingPartitions": 0,
            "Status": 1,
            "CreatedTopics": 0,
            "VpcId": "xx",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "InstanceId": "xx",
            "Vip": "xx",
            "SubnetId": "xx",
            "InstanceType": "xx",
            "RemainderTopics": 17,
            "MaxConnection": 1,
            "PublicNetwork": 48000,
            "Healthy": 1,
            "ZoneId": 100003,
            "Cvm": 0,
            "DiskSize": 120000,
            "HealthyMessage": "xx",
            "RemainderPartitions": 45,
            "InstanceName": "xx",
            "CreatedPartitions": 0,
            "Features": [
                "xx"
            ],
            "ZoneIds": [
                0
            ],
            "ExpireTime": 1,
            "Bandwidth": 48000,
            "MaxGroupNum": 0,
            "RetentionTimeConfig": {
                "StepForwardPercentage": 10,
                "DiskQuotaPercentage": 90,
                "Enable": 0,
                "BottomRetention": 360
            },
            "DynamicDiskConfig": {
                "Enable": 1,
                "DiskQuotaPercentage": 30,
                "StepForwardPercentage": 15,
                "MaxDiskSpace": 1000
            },
            "Vport": "xx",
            "CreateTime": 1,
            "VipList": [
                {
                    "Vip": "xx",
                    "Vport": "xx"
                }
            ],
            "RemainingTopics": 0
        },
        "RequestId": "xx"
    }
}
```

