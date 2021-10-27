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
        "RequestId": "89d4c4cd-9e03-4574-88bb-98b5115334ac",
        "TotalCount": 1,
        "Namespaces": [
            {}
        ]
    }
}
```

