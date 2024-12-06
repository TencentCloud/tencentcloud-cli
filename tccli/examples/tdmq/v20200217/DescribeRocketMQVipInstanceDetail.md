**Example 1: 获取单个RocketMQ专享集群信息**



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
            "ClusterId": "rocketmq-rd3545bkkj49",
            "ClusterName": "rocket-order-cluster",
            "Region": "华南地区",
            "CreateTime": 1729478721,
            "Remark": "info- remark",
            "PublicEndPoint": "rocketmq.access.public.com:9867",
            "VpcEndPoint": "rocketmq.resource.vpc.com:5010",
            "SupportNamespaceEndpoint": true,
            "Vpcs": [
                {
                    "VpcId": "vpc-9dlrd5h1",
                    "SubnetId": "subnet-jadmas"
                }
            ],
            "IsVip": true,
            "RocketMQFlag": true,
            "Status": 1,
            "IsolateTime": 1729478721,
            "HttpPublicEndpoint": "http://rocketmq.access.public.com:9867",
            "HttpVpcEndpoint": "http://rocketmq.resource.vpc.com:5010",
            "InternalEndpoint": "rocketmq.tencent.internal.com:8080",
            "HttpInternalEndpoint": "http://rocketmq.tencent.internal.com:8080",
            "AclEnabled": true,
            "PublicClbId": "",
            "Vip": "",
            "VpcId": "",
            "SupportMigration": true,
            "InstanceStatus": 1,
            "ZoneId": 100001,
            "ZoneIds": [
                100001
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
            "ConfigDisplay": "",
            "NodeCount": 1,
            "NodeDistribution": [
                {
                    "ZoneName": "广东一区",
                    "ZoneId": "100001",
                    "NodeCount": 1
                }
            ],
            "TopicDistribution": [
                {
                    "TopicType": "normal",
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
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

