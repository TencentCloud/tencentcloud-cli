**Example 1: 查询流量包列表**



Input: 

```
tccli cdn DescribeTrafficPackages --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "604e7ebe-041c-4684-ab59-e0c825c3a788",
        "TrafficPackages": [
            {
                "Id": 888890106,
                "Type": "日常流量包",
                "ConfigId": 672,
                "Bytes": 100000000000,
                "BytesUsed": 0,
                "Status": "enabled",
                "CreateTime": "2021-11-10 17:59:24",
                "EnableTime": "2021-11-01 00:00:00",
                "ExpireTime": "2022-10-31 23:59:59",
                "ContractExtension": false,
                "AutoExtension": true,
                "ExtensionMode": 3,
                "Area": "mainland",
                "LifeTimeMonth": 12,
                "RefundAvailable": false,
                "Channel": "ACTIVE_PURCHASE",
                "ExtensionAvailable": true,
                "Region": 0
            }
        ],
        "TotalCount": 6,
        "ExpiringCount": 0,
        "EnabledCount": 6,
        "PaidCount": 6
    }
}
```

