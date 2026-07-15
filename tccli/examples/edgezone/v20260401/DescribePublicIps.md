**Example 1: 查询静态公网实例Ip信息**



Input: 

```
tccli edgezone DescribePublicIps --cli-unfold-argument  \
    --ZoneId ap-beijing \
    --State InUse \
    --Type Ipv4 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-028",
        "TotalCount": 2,
        "IpInfoSet": [
            {
                "Ip": "10.0.0.200",
                "NetworkInstanceId": "epn-xxxxxxxx",
                "InstanceId": "ins-001",
                "State": "InUse",
                "Type": "Ipv4",
                "CreatedAt": "2026-04-07T00:00:00",
                "UpdatedAt": "2026-04-07T00:00:00"
            },
            {
                "Ip": "10.0.0.201",
                "NetworkInstanceId": "epn-xxxxxxxx",
                "InstanceId": "",
                "State": "Unbound",
                "Type": "Ipv4",
                "CreatedAt": "2026-04-07T00:00:00",
                "UpdatedAt": "2026-04-07T00:00:00"
            }
        ]
    }
}
```

