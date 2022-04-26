**Example 1: 获取用户命名空间列表**



Input: 

```
tccli tdmq DescribeRocketMQNamespaces --cli-unfold-argument  \
    --ClusterId rocketmq-rd3545bkkj49 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Namespaces": [
            {
                "Remark": "xx",
                "PublicEndpoint": "xx",
                "RetentionTime": 1,
                "VpcEndpoint": "xx",
                "Ttl": 1,
                "NamespaceId": "xx"
            }
        ]
    }
}
```

