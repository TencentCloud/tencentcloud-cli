**Example 1: 地址池详情**



Input: 

```
tccli igtm DescribeAddressPoolDetail --cli-unfold-argument  \
    --PoolId 1
```

Output: 
```
{
    "Response": {
        "AddressPool": {
            "PoolId": 1,
            "PoolName": "测试地址池",
            "TrafficStrategy": "ALL",
            "MonitorId": 1,
            "CreatedOn": "2020-09-22T00:00:00+00:00",
            "UpdatedOn": "2020-09-22T00:00:00+00:00"
        },
        "AddressSet": [
            {
                "AddressId": 1,
                "Addr": "1.1.1.2",
                "Location": "上好电信",
                "Status": "OK",
                "IsEnable": "ENABLED",
                "Weight": 1,
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "UpdatedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

