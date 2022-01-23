**Example 1: 获取实例列表详情**



Input: 

```
tccli ckafka DescribeInstancesDetail --cli-unfold-argument  \
    --InstanceId instance-will-s \
    --SearchWord tre \
    --Offset 0 \
    --Limit 10 \
    --Status 0 1 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "InstanceList": [
                {
                    "MaxTopicNumber": 0,
                    "RenewFlag": 0,
                    "DiskType": "xx",
                    "Version": "xx",
                    "RebalanceTime": "xx",
                    "Status": 1,
                    "VpcId": "xx",
                    "Tags": [
                        {
                            "TagKey": "xx",
                            "TagValue": "xx"
                        }
                    ],
                    "InstanceId": "xx",
                    "IsInternal": 0,
                    "Vip": "xx",
                    "TopicNum": 0,
                    "SubnetId": "xx",
                    "InstanceType": "xx",
                    "PublicNetwork": 0,
                    "Healthy": 0,
                    "ZoneId": 0,
                    "PublicNetworkChargeType": "xx",
                    "Cvm": 0,
                    "DiskSize": 0,
                    "HealthyMessage": "xx",
                    "InstanceName": "xx",
                    "MaxPartitionNumber": 0,
                    "PartitionNumber": 1,
                    "ZoneIds": [
                        0
                    ],
                    "ExpireTime": 0,
                    "Bandwidth": 0,
                    "Vport": "xx",
                    "CreateTime": 0,
                    "VipList": [
                        {
                            "Vip": "xx",
                            "Vport": "xx"
                        }
                    ]
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

