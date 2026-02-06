**Example 1: 创建消费组**

创建消费组

Input: 

```
tccli cls CreateConsumerGroup --cli-unfold-argument  \
    --ConsumerGroup test-123 \
    --Timeout 1 \
    --Topics 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3
```

Output: 
```
{
    "Response": {
        "ConsumerGroup": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3",
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1xx"
    }
}
```

