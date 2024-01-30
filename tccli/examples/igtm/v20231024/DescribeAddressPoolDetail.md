**Example 1: 地址池详情**



Input: 

```
tccli igtm DescribeAddressPoolDetail --cli-unfold-argument  \
    --PoolId 0
```

Output: 
```
{
    "Response": {
        "AddressPool": {
            "PoolId": 1,
            "PoolName": "abc",
            "TrafficStrategy": "abc",
            "MonitorId": 1,
            "CreatedOn": "2020-09-22T00:00:00+00:00",
            "UpdatedOn": "2020-09-22T00:00:00+00:00"
        },
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
        "RequestId": "abc"
    }
}
```

