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
                    "ClusterId": "rocketmq-a52qova7x97b",
                    "ClusterName": "test_name",
                    "Region": "ap-beijing",
                    "Status": 0,
                    "AclEnabled": true,
                    "CreateTime": 1620321019000,
                    "Remark": "remark info",
                    "PublicEndPoint": "pulsar://rocketmq-xxxx1.xxxx.com:5678",
                    "VpcEndPoint": "pulsar://rocketmq-xxxx1.xxxx.com:5678",
                    "HttpPublicEndpoint": "http://rocketmq-c1.public.com:5678",
                    "HttpVpcEndpoint": "http://rocketmq-c1.vpc.com:5678",
                    "InternalEndpoint": "http://rocketmq-c1.internal.com:5678",
                    "HttpInternalEndpoint": "",
                    "Vpcs": [
                        {
                            "SubnetId": "mqsubnet32id",
                            "VpcId": "vpcmqid62a"
                        }
                    ],
                    "SupportNamespaceEndpoint": true,
                    "RocketMQFlag": true,
                    "IsolateTime": 0,
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
                    "TopicDistribution": [
                        {
                            "TopicType": "Normal",
                            "Count": 1
                        }
                    ],
                    "MaxQueuesPerTopic": 1,
                    "MaxNamespaceNum": 10
                }
            }
        ]
    }
}
```

