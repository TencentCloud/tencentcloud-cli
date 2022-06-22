**Example 1: 设置自动续费**



Input: 

```
tccli postgres SetAutoRenewFlag --cli-unfold-argument  \
    --AutoRenewFlag 1 \
    --DBInstanceIdSet postgres-6fego161
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "Count": 1
    }
}
```

