**Example 1: 实例列表**



Input: 

```
tccli igtm DescribeInstanceList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name Domain \
    --Filters.0.Value gtmtest.com \
    --Filters.0.Fuzzy True
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "gtm-dsdd123xdo",
                "InstanceName": "gtm测试实例",
                "Domain": "gtmtest.com",
                "AccessType": "CUSTOM",
                "AccessDomain": "igtm-access",
                "AccessSubDomain": "gtmtest.com",
                "GlobalTtl": 600,
                "PackageType": "ULTIMATE",
                "WorkingStatus": "UNKNOWN",
                "Status": "ENABLED",
                "Remark": "测试实例",
                "StrategyNum": 0,
                "AddressPoolNum": 0,
                "MonitorNum": 0,
                "CreatedOn": "2024-07-19 15:40:19",
                "UpdatedOn": "2024-07-19 15:40:19",
                "ResourceId": "ins-oxrvmnl4yrd"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

