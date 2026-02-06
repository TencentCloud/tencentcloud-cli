**Example 1: 删除消费组**

删除消费组

Input: 

```
tccli cls DeleteConsumerGroup --cli-unfold-argument  \
    --ConsumerGroup test-123 \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3
```

Output: 
```
{
    "Response": {
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
    }
}
```

