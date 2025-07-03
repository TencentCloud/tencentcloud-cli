**Example 1: 地址池列表**



Input: 

```
tccli igtm DescribeAddressPoolList --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Value abc \
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
                "PoolName": "abc",
                "TrafficStrategy": "abc",
                "MonitorId": 1,
                "Status": "abc",
                "AddressNum": 0,
                "MonitorGroupNum": 0,
                "MonitorTaskNum": 0,
                "AddressSet": [
                    {
                        "AddressId": 1,
                        "Addr": "abc",
                        "Location": "abc",
                        "Status": "abc",
                        "IsEnable": "abc",
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
        "RequestId": "abc"
    }
}
```

