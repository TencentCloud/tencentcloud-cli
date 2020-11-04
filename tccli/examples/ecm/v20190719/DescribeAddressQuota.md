**Example 1: 查询弹性公网IP配额**



Input: 

```
tccli ecm DescribeAddressQuota --cli-unfold-argument  \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "TOTAL_EIP_QUOTA",
                "QuotaCurrent": 0,
                "QuotaLimit": 20
            },
            {
                "QuotaId": "DAILY_EIP_APPLY",
                "QuotaCurrent": 0,
                "QuotaLimit": 40
            },
            {
                "QuotaId": "DAILY_EIP_ASSIGN",
                "QuotaCurrent": 0,
                "QuotaLimit": 40
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

