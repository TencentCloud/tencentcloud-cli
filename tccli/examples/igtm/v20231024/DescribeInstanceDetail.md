**Example 1: 实例详情**



Input: 

```
tccli igtm DescribeInstanceDetail --cli-unfold-argument  \
    --InstanceId gtm-dsdd123xdo
```

Output: 
```
{
    "Response": {
        "Instance": {
            "InstanceId": "gtm-dsdd123xdo",
            "InstanceName": "测试实例",
            "Domain": "gtmtest.com",
            "AccessType": "CUSTOM",
            "AccessSubDomain": "access-gtm",
            "AccessDomain": "gtmtest.com",
            "GlobalTtl": 600,
            "PackageType": "ULTIMATE",
            "WorkingStatus": "NORMAL",
            "Status": "ENABLED",
            "IsCnameConfigured": false,
            "Remark": "备注信息",
            "StrategyNum": 0,
            "AddressPoolNum": 0,
            "MonitorNum": 0,
            "ResourceId": "ins-oxrvmnl4yrd",
            "NotifyEventSet": [],
            "CreatedOn": "2024-07-19 15:40:19",
            "UpdatedOn": "2024-07-19 15:40:19"
        },
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

