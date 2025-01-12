**Example 1: 查询互联网通道路由列表**

查询互联网通道路由列表

Input: 

```
tccli dc DescribePublicDirectConnectTunnelRoutes --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-69p738pu
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "RouteId": "ipv4-l4udy3uj",
                "DestinationCidrBlock": "49.7.252.80/30",
                "RouteType": "STATIC",
                "Status": "ENABLE",
                "ASPath": [],
                "NextHop": "10.60.191.1",
                "UpdateTime": "2023-01-13 22:48:50",
                "ApplyOnTunnelEnable": true
            }
        ],
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea",
        "TotalCount": 1
    }
}
```

