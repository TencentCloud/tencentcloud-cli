**Example 1: test**



Input: 

```
tccli tdmq UpdateTenantQuotaOpt --cli-unfold-argument  \
    --CustomerAppId 251199683 \
    --CustomerUin 100000122146 \
    --MaxNamespaces 10 \
    --MaxPartitions 256000 \
    --MaxRetention 1296000000 \
    --MaxTopics 1000 \
    --TenantId rocketmq-w7e73xbxqw5k
```

Output: 
```
{
    "Response": {
        "RequestId": "029f3725-9dab-4f79-870e-b37d43704b7f"
    }
}
```

