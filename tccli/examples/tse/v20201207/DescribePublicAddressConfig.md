**Example 1: 查询网关公网地址列表**



Input: 

```
tccli tse DescribePublicAddressConfig --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03767",
            "ConfigList": [
                {
                    "Vip": "1.1.1.1",
                    "InternetMaxBandwidthOut": 1,
                    "GroupId": "group-4se0czf7",
                    "GroupName": "公网入口分组"
                }
            ]
        },
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

