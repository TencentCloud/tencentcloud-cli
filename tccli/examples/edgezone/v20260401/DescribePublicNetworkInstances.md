**Example 1: 根据可用区ID查询公网实例**



Input: 

```
tccli edgezone DescribePublicNetworkInstances --cli-unfold-argument  \
    --ZoneId ap-beijing \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-003",
        "TotalCount": 2,
        "PublicNetworkInstanceSet": [
            {
                "NetworkInstanceId": "epn-a1b2c3d4",
                "ZoneId": "ap-beijing",
                "NetworkInstanceName": "test-bgp-instance",
                "Bandwidth": 100,
                "Line": "BGP",
                "RouteMode": "BGP",
                "Ipv4CidrSet": [
                    {
                        "Cidr": "10.0.0.128/26",
                        "Gateway": "10.0.0.129"
                    }
                ],
                "Ipv6CidrSet": [
                    {
                        "Cidr": "2001:db8::/96",
                        "Gateway": "2001:db8::1"
                    }
                ],
                "ServerCount": 2,
                "Ipv4Count": 61,
                "Ipv6Count": -1,
                "CreatedAt": "2026-04-07T00:00:00",
                "UpdatedAt": "2026-04-07T00:00:00"
            }
        ]
    }
}
```

