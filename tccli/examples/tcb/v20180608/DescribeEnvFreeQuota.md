**Example 1: 拉取该环境下所有后付费配额**



Input: 

```
tccli tcb DescribeEnvFreeQuota --cli-unfold-argument  \
    --EnvId env-id
```

Output: 
```
{
    "Response": {
        "QuotaItems": [],
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

