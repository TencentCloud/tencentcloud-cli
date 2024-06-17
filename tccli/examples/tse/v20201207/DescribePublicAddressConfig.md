**Example 1: 查询网关公网地址列表**



Input: 

```
tccli tse DescribePublicAddressConfig --cli-unfold-argument  \
    --GatewayId abc \
    --GroupId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "ConfigList": [
                {
                    "Vip": "1.1.1.1",
                    "InternetMaxBandwidthOut": 1,
                    "GroupId": "abc",
                    "GroupName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

