**Example 1: 获取指定消费组下当前客户端的连接情况**



Input: 

```
tccli tdmq DescribeRocketMQConsumerConnections --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --GroupId test_group
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Connections": [
            {
                "ClientId": "9.43.174.90@18834#7187709773375173",
                "ClientAddr": "9.43.174.90",
                "Language": "JAVA",
                "Accumulative": 300,
                "Version": "V4.9.7"
            }
        ],
        "GroupDetail": {
            "Name": "test_group",
            "ConsumerNum": 1,
            "TotalAccumulative": 300,
            "ConsumptionMode": -1,
            "BroadcastEnabled": false,
            "ReadEnabled": true,
            "RetryPartitionNum": 1,
            "CreateTime": 1727075298000,
            "UpdateTime": 1727075298000,
            "ClientProtocol": "TCP",
            "Remark": "测试消费组",
            "ConsumerType": "PUSH",
            "GroupType": "TCP",
            "RetryMaxTimes": 16,
            "InstanceId": "rocketmq-2p9vx3ax9jxg",
            "Namespace": "test_namespace",
            "TPS": 10
        },
        "RequestId": "abc"
    }
}
```

