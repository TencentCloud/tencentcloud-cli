**Example 1: 获取实例列表详情**

1

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
            "TotalCount": 0,
            "InstanceList": [
                {
                    "InstanceId": "xx",
                    "InstanceName": "xx",
                    "Vip": "xx",
                    "Vport": "xx",
                    "VipList": [
                        {
                            "Vip": "xx",
                            "Vport": "xx"
                        }
                    ],
                    "Status": 0,
                    "Bandwidth": 0,
                    "DiskSize": 0,
                    "ZoneId": 0,
                    "VpcId": "xx",
                    "SubnetId": "xx",
                    "RenewFlag": 0,
                    "Healthy": 0,
                    "HealthyMessage": "xx",
                    "CreateTime": 0,
                    "ExpireTime": 0,
                    "IsInternal": 0,
                    "TopicNum": 0,
                    "Tags": [
                        {
                            "TagKey": "xx",
                            "TagValue": "xx"
                        }
                    ],
                    "Version": "xx",
                    "ZoneIds": [
                        0
                    ],
                    "Cvm": 0,
                    "InstanceType": "xx",
                    "DiskType": "xx",
                    "MaxTopicNumber": 0,
                    "MaxPartitionNumber": 0,
                    "RebalanceTime": "xx",
                    "PartitionNumber": 1,
                    "PublicNetworkChargeType": "xx",
                    "PublicNetwork": 0,
                    "ClusterType": "xx",
                    "Features": [
                        "xx"
                    ]
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

