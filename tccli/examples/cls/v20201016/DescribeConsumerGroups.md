**Example 1: 查询消费组信息**

查询消费组信息

Input: 

```
tccli cls DescribeConsumerGroups --cli-unfold-argument  \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --Topics 6f6ded3f-948c-4616-9c7c-956a95d8c1a3
```

Output: 
```
{
    "Response": {
        "ConsumerGroupsInfo": [
            {
                "ConsumerGroup": "test-123",
                "Timeout": 1,
                "Topics": [
                    "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
                ]
            }
        ],
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
    }
}
```

