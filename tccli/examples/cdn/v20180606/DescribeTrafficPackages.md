**Example 1: 境内流量包查询**



Input: 

```
tccli cdn DescribeTrafficPackages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "bc7df980-c745-4f80-854e-1a49295b0d5f",
        "TrafficPackages": [
            {
                "Id": 123,
                "Type": "新手流量包",
                "Bytes": 50000000000,
                "BytesUsed": 0,
                "Status": "expired",
                "CreateTime": "2017-07-31 09:28:14",
                "EnableTime": "2017-07-01 00:00:00",
                "ExpireTime": "2017-08-01 00:00:00",
                "ContractExtension": false,
                "AutoExtension": false,
                "Channel": "cdn",
                "Area": "mainland",
                "LifeTimeMonth": 1,
                "ExtensionAvailable": false
            }
        ],
        "TotalCount": 40,
        "ExpiringCount": 0,
        "EnabledCount": 40
    }
}
```

