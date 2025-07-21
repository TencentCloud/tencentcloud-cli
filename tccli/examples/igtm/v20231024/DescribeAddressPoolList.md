**Example 1: 地址池列表**



Input: 

```
tccli igtm DescribeAddressPoolList --cli-unfold-argument  \
    --Filters.0.Name PoolName \
    --Filters.0.Value gtm-dnspod \
    --Filters.0.Fuzzy True \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AddressPoolSet": [
            {
                "PoolId": 1,
                "PoolName": "gtm-dnspod",
                "TrafficStrategy": "WEIGHT",
                "MonitorId": 1,
                "Status": "WARN",
                "AddressNum": 0,
                "MonitorGroupNum": 0,
                "MonitorTaskNum": 0,
                "AddressSet": [
                    {
                        "AddressId": 1,
                        "Addr": "1.1.1.2",
                        "Location": "上海电信",
                        "Status": "UNMONITORED",
                        "IsEnable": "ENABLED",
                        "Weight": 1,
                        "CreatedOn": "2020-09-22T00:00:00+00:00",
                        "UpdatedOn": "2020-09-22T00:00:00+00:00"
                    }
                ],
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "UpdatedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

