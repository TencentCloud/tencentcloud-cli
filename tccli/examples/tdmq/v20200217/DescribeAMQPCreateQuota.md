**Example 1: 获取用户配额**



Input: 

```
tccli tdmq DescribeAMQPCreateQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MaxClusterNum": 1,
        "ExchangeCapacity": 1,
        "QueueCapacity": 1,
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "UsedClusterNum": 1,
        "MaxTpsPerVHost": 1
    }
}
```

