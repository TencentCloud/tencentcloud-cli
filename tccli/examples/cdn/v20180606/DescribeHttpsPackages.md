**Example 1: HTTPS请求包查询**

HTTPS请求包查询

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
        "RequestId": "521e16c1a2c389fa34ff23aafa0db726",
        "HttpsPackages": [
            {
                "Id": 5720,
                "Type": "日常HTTPS请求包",
                "ConfigId": 672,
                "Size": 10000000,
                "SizeUsed": 0,
                "Status": "frozen",
                "CreateTime": "2023-07-05 15:41:26",
                "EnableTime": "2023-07-05 15:00:00",
                "ExpireTime": "2024-07-05 15:00:00",
                "LifeTimeMonth": 12,
                "RefundAvailable": false,
                "Channel": "ACTIVE_PURCHASE",
                "TrueEnableTime": "2023-07-05 15:00:00",
                "TrueExpireTime": "2024-07-05 15:59:59",
                "Area": "global",
                "ContractExtension": false,
                "AutoExtension": false,
                "ExtensionMode": 0,
                "ExtensionAvailable": false
            }
        ],
        "TotalCount": 1,
        "ExpiringCount": 0,
        "EnabledCount": 0,
        "PaidCount": 1
    }
}
```

