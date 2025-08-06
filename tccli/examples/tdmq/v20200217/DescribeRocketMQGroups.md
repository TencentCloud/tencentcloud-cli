**Example 1: 查询订阅组列表**



Input: 

```
tccli tdmq DescribeRocketMQGroups --cli-unfold-argument  \
    --ClusterId rocketmq-4k4orqgq \
    --NamespaceId test_namespace \
    --Offset 0 \
    --Limit 20 \
    --FilterTopic test_topic \
    --FilterGroup test_group \
    --SortedBy tps \
    --SortOrder asc \
    --FilterOneGroup test_group \
    --Types TCP
```

Output: 
```
{
    "Response": {
        "RequestId": "1c127300-fcdd-4087-b1d2-fd75a1cefbe4",
        "TotalCount": 1,
        "Groups": [
            {
                "InstanceId": "rocketmq-4k4orqgq",
                "Namespace": "test_ns",
                "Name": "test_group",
                "ConsumerNum": 1,
                "TotalAccumulative": 380,
                "RetryMaxTimes": 10,
                "ConsumptionMode": -1,
                "BroadcastEnabled": false,
                "ReadEnabled": true,
                "RetryPartitionNum": 1,
                "CreateTime": 1621307489000,
                "UpdateTime": 1621307706000,
                "ClientProtocol": "TCP",
                "Remark": "测试消费组",
                "ConsumerType": "PUSH",
                "TPS": 20,
                "GroupType": "TCP",
                "SubscribeTopicNum": "1"
            }
        ]
    }
}
```

