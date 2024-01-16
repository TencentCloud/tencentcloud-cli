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
            "TotalCount": 0,
            "InstanceList": [
                {
                    "InstanceId": "abc",
                    "InstanceName": "abc",
                    "Vip": "abc",
                    "Vport": "abc",
                    "VipList": [
                        {
                            "Vip": "abc",
                            "Vport": "abc"
                        }
                    ],
                    "Status": 0,
                    "Bandwidth": 0,
                    "DiskSize": 0,
                    "ZoneId": 0,
                    "VpcId": "abc",
                    "SubnetId": "abc",
                    "RenewFlag": 0,
                    "Healthy": 0,
                    "HealthyMessage": "abc",
                    "CreateTime": 0,
                    "ExpireTime": 0,
                    "IsInternal": 0,
                    "TopicNum": 0,
                    "Tags": [
                        {
                            "TagKey": "abc",
                            "TagValue": "abc"
                        }
                    ],
                    "Version": "abc",
                    "ZoneIds": [
                        0
                    ],
                    "Cvm": 0,
                    "InstanceType": "abc",
                    "DiskType": "abc",
                    "MaxTopicNumber": 0,
                    "MaxPartitionNumber": 0,
                    "RebalanceTime": "abc",
                    "PartitionNumber": 1,
                    "PublicNetworkChargeType": "abc",
                    "PublicNetwork": 0,
                    "ClusterType": "abc",
                    "Features": [
                        "abc"
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

