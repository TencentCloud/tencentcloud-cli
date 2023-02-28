**Example 1: HTTPS请求包查询**



Input: 

```
tccli cdn DescribeHttpsPackages --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "HttpsPackages": [
            {
                "Status": "enable",
                "EnableTime": "2023-02-10 00:00:00",
                "SizeUsed": 100,
                "ExpireTime": "2023-03-10 00:00:00",
                "Area": "global",
                "TrueExpireTime": "2023-03-31 23:59:59",
                "TrueEnableTime": "2023-02-01 00:00:00",
                "Id": 1,
                "LifeTimeMonth": 12,
                "ExtensionAvailable": true,
                "ExtensionMode": 1,
                "RefundAvailable": false,
                "ContractExtension": true,
                "ConfigId": 661,
                "Type": "HTTPS请求包",
                "CreateTime": "2023-02-10 00:00:00",
                "Channel": "ACTIVE_PURCHASE",
                "Size": 10000
            }
        ],
        "ExpiringCount": 0,
        "TotalCount": 1,
        "EnabledCount": 1,
        "RequestId": "eb308d9a-6c72-4f23-aed6-b06b5a481047",
        "PaidCount": 1
    }
}
```

