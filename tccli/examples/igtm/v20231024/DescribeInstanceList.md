**Example 1: 实例列表**



Input: 

```
tccli igtm DescribeInstanceList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Value abc \
    --Filters.0.Fuzzy True
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Domain": "abc",
                "AccessType": "abc",
                "AccessDomain": "abc",
                "AccessSubDomain": "abc",
                "GlobalTtl": 0,
                "PackageType": "abc",
                "WorkingStatus": "abc",
                "Status": "abc",
                "Remark": "abc",
                "StrategyNum": 0,
                "AddressPoolNum": 0,
                "MonitorNum": 0,
                "CreatedOn": "abc",
                "UpdatedOn": "abc",
                "ResourceId": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

