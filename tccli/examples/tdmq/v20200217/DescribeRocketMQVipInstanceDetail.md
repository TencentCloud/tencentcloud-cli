**Example 1: huo**



Input: 

```
tccli tdmq DescribeRocketMQVipInstanceDetail --cli-unfold-argument  \
    --ClusterId rocketmq-rd3545bkkj49
```

Output: 
```
{
    "Response": {
        "RequestId": "c6d158b6-89b2-40d1-b1f6-5973f0f00cd5",
        "ClusterInfo": {
            "ClusterId": "rocketmq-rd3545bkkj49",
            "ClusterName": "test-example",
            "Region": "ap-beijing",
            "CreateTime": 1620321019000,
            "SupportNamespaceEndpoint": true,
            "Remark": "modified",
            "PublicEndPoint": "pulsar://xxxxx.com:6650",
            "Vpcs": [
                {
                    "SubnetId": "xx",
                    "VpcId": "xx"
                }
            ],
            "IsVip": true,
            "RocketMQFlag": true,
            "VpcEndPoint": "pulsar://xxxxx.com:6650"
        },
        "InstanceConfig": {
            "MaxTpsPerNamespace": 8000,
            "UsedNamespaceNum": 1,
            "MaxTopicNum": 1000,
            "UsedTopicNum": 2,
            "MaxGroupNum": 10000,
            "UsedGroupNum": 1,
            "MaxNamespaceNum": 10,
            "ConfigDisplay": "xx",
            "NodeCount": 2,
            "NodeDistribution": [],
            "TopicDistribution": []
        }
    }
}
```

