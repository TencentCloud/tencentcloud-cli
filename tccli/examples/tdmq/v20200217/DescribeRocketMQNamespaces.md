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
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7",
        "Namespaces": [
            {
                "Remark": "info-remark",
                "PublicEndpoint": "http://public.test.com",
                "RetentionTime": 1,
                "VpcEndpoint": "http://vpc.test.com",
                "Ttl": 1,
                "NamespaceId": "ordernamespace",
                "InternalEndpoint": "http://internal.test.com"
            }
        ]
    }
}
```

