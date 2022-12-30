**Example 1: 获取主题列表**



Input: 

```
tccli tdmq DescribeRocketMQTopics --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example
```

Output: 
```
{
    "Response": {
        "RequestId": "c017c4d1-13cb-4f14-ab89-2c6530892f90",
        "TotalCount": 1,
        "Topics": [
            {
                "Name": "example-topic",
                "Type": "Normal",
                "GroupNum": 0,
                "Remark": "modified",
                "PartitionNum": 3,
                "CreateTime": 1621308465000,
                "UpdateTime": 1621308657000
            }
        ]
    }
}
```

