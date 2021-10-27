**Example 1: 查询订阅组列表**



Input: 

```
tccli tdmq DescribeRocketMQGroups --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1c127300-fcdd-4087-b1d2-fd75a1cefbe4",
        "TotalCount": 1,
        "Groups": [
            {}
        ]
    }
}
```

