**Example 1: 查询流量包列表**

查询流量包列表

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
        "RequestId": "b1a70a67f5500913be355ac2f09ff191",
        "TrafficPackages": [
            {
                "Id": 22890370,
                "Type": "日常流量包",
                "ConfigId": 672,
                "Bytes": 100000000000,
                "BytesUsed": 0,
                "Status": "frozen",
                "CreateTime": "2022-11-11 15:52:28",
                "EnableTime": "2022-11-11 15:00:00",
                "ExpireTime": "2023-11-11 15:00:00",
                "ContractExtension": false,
                "AutoExtension": false,
                "ExtensionMode": 0,
                "Area": "mainland",
                "LifeTimeMonth": 12,
                "RefundAvailable": false,
                "Channel": "ACTIVE_PURCHASE",
                "ExtensionAvailable": false,
                "Region": 0,
                "TrueEnableTime": "2022-11-11 15:00:00",
                "TrueExpireTime": "2023-11-11 15:59:59"
            }
        ],
        "TotalCount": 1,
        "ExpiringCount": 0,
        "EnabledCount": 0,
        "PaidCount": 1
    }
}
```

