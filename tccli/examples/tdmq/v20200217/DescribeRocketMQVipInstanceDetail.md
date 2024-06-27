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
        "ClusterInfo": {
            "ClusterId": "abc",
            "ClusterName": "abc",
            "Region": "abc",
            "CreateTime": 1,
            "Remark": "abc",
            "PublicEndPoint": "abc",
            "VpcEndPoint": "abc",
            "SupportNamespaceEndpoint": true,
            "Vpcs": [
                {
                    "VpcId": "abc",
                    "SubnetId": "abc"
                }
            ],
            "IsVip": true,
            "RocketMQFlag": true,
            "Status": 0,
            "IsolateTime": 0,
            "HttpPublicEndpoint": "abc",
            "HttpVpcEndpoint": "abc",
            "InternalEndpoint": "abc",
            "HttpInternalEndpoint": "abc",
            "AclEnabled": true,
            "PublicClbId": "abc",
            "Vip": "abc",
            "VpcId": "abc",
            "SupportMigration": true,
            "InstanceStatus": 0,
            "ZoneId": 0,
            "ZoneIds": [
                0
            ]
        },
        "InstanceConfig": {
            "MaxTpsPerNamespace": 1,
            "MaxNamespaceNum": 1,
            "UsedNamespaceNum": 1,
            "MaxTopicNum": 1,
            "UsedTopicNum": 1,
            "MaxGroupNum": 1,
            "UsedGroupNum": 1,
            "ConfigDisplay": "abc",
            "NodeCount": 1,
            "NodeDistribution": [
                {
                    "ZoneName": "abc",
                    "ZoneId": "abc",
                    "NodeCount": 1
                }
            ],
            "TopicDistribution": [
                {
                    "TopicType": "abc",
                    "Count": 1
                }
            ],
            "MaxQueuesPerTopic": 1,
            "MaxRetention": 0,
            "MinRetention": 0,
            "Retention": 0,
            "TopicNumLowerLimit": 0,
            "TopicNumUpperLimit": 0
        },
        "RequestId": "abc"
    }
}
```

