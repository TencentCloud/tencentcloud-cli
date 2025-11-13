**Example 1: 获取主题列表**



Input: 

```
tccli tdmq DescribeRocketMQTopics --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_ns \
    --FilterGroup test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "c017c4d1-13cb-4f14-ab89-2c6530892f90",
        "TotalCount": 1,
        "Topics": [
            {
                "Name": "test_topic",
                "Type": "Normal",
                "GroupNum": 1,
                "Remark": "测试主题",
                "PartitionNum": 3,
                "CreateTime": 1621308465000,
                "UpdateTime": 1621308657000,
                "InstanceId": "rocketmq-2p9vx3ax9jxg",
                "Namespace": "test_ns"
            }
        ]
    }
}
```

