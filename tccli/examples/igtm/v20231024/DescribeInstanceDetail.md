**Example 1: 实例详情**

{
  "InstanceId": "abc"
}

Input: 

```
tccli igtm DescribeInstanceDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Instance": {
            "InstanceId": "abc",
            "InstanceName": "abc",
            "Domain": "abc",
            "AccessType": "abc",
            "AccessSubDomain": "abc",
            "AccessDomain": "abc",
            "GlobalTtl": 1,
            "PackageType": "abc",
            "WorkingStatus": "abc",
            "Status": "abc",
            "IsCnameConfigured": true,
            "Remark": "abc",
            "StrategyNum": 0,
            "AddressPoolNum": 0,
            "MonitorNum": 0,
            "ResourceId": "abc",
            "NotifyEventSet": [
                "abc"
            ],
            "CreatedOn": "abc",
            "UpdatedOn": "abc"
        },
        "RequestId": "abc"
    }
}
```

