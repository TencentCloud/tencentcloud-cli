**Example 1: 获取用户创建的集群信息列表**



Input: 

```
tccli tdmq DescribeRocketMQClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1faeceb2-eaa9-407e-bd9a-d3eff76ca882",
        "TotalCount": 1,
        "ClusterList": [
            {}
        ]
    }
}
```

