**Example 1: 获取用户创建的集群信息列表**



Input: 

```
tccli tdmq DescribeRocketMQClusters --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1faeceb2-eaa9-407e-bd9a-d3eff76ca882",
        "TotalCount": 1,
        "ClusterList": [
            {
                "Info": {
                    "ClusterId": "rocketmq-xxxx1",
                    "ClusterName": "test",
                    "Region": "ap-beijing",
                    "CreateTime": 1620321019000,
                    "Remark": "字符串",
                    "PublicEndPoint": "pulsar://rocketmq-xxxx1.xxxx.com:5678",
                    "VpcEndPoint": "pulsar://rocketmq-xxxx1.xxxx.com:5678",
                    "Vpcs": [
                        {
                            "SubnetId": "xx",
                            "VpcId": "xx"
                        }
                    ],
                    "SupportNamespaceEndpoint": true,
                    "RocketMQFlag": true,
                    "IsVip": true
                },
                "Config": {
                    "MaxTpsPerNamespace": 8000,
                    "UsedNamespaceNum": 1,
                    "MaxTopicNum": 1000,
                    "UsedTopicNum": 2,
                    "MaxGroupNum": 10000,
                    "UsedGroupNum": 1,
                    "MaxRetentionTime": 1296000000,
                    "MaxLatencyTime": 3456000000,
                    "MaxNamespaceNum": 10
                }
            }
        ]
    }
}
```

