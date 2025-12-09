**Example 1: 获取RocketMQ集群详情**

获取RocketMQ集群详情

Input: 

```
tccli tdmq DescribeRocketMQCluster --cli-unfold-argument  \
    --ClusterId rocketmq-rd3545bkkj49
```

Output: 
```
{
    "Response": {
        "RequestId": "c6d158b6-89b2-40d1-b1f6-5973f0f00cd5",
        "ClusterInfo": {
            "ClusterId": "rocketmq-rd3545bkkj49",
            "ClusterName": "test-name",
            "Region": "ap-beijing",
            "CreateTime": 1620321019000,
            "Remark": "test remark info.",
            "PublicEndPoint": "",
            "VpcEndPoint": "http://MQ_INST_rocketmqrd3545bkkj49_test_ns.tdmq-rocketmq.qcloud.tencenttdmq.com:3000",
            "Vpcs": [
                {
                    "SubnetId": "subnet-123",
                    "VpcId": "vpc-12333"
                }
            ],
            "SupportNamespaceEndpoint": true,
            "RocketMQFlag": true,
            "IsVip": true,
            "IsolateTime": 0,
            "Status": 1,
            "AclEnabled": true,
            "InternalEndpoint": "",
            "HttpInternalEndpoint": "",
            "HttpVpcEndpoint": "",
            "HttpPublicEndpoint": ""
        },
        "ClusterConfig": {
            "MaxTpsPerNamespace": 8000,
            "MaxTpsLimit": 8000,
            "UsedNamespaceNum": 1,
            "MaxTopicNum": 1000,
            "UsedTopicNum": 2,
            "MaxGroupNum": 10000,
            "UsedGroupNum": 1,
            "MaxRetentionTime": 1296000000,
            "MaxLatencyTime": 3456000000,
            "MaxNamespaceNum": 10,
            "MaxQueuesPerTopic": 1,
            "TopicDistribution": []
        },
        "ClusterStats": {
            "TopicNum": 2,
            "ProducedMsgNum": 0,
            "ConsumedMsgNum": 0,
            "AccumulativeMsgNum": 0
        }
    }
}
```

