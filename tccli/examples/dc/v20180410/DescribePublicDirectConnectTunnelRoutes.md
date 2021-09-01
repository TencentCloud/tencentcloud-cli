**Example 1: 查询互联网通道路由列表**



Input: 

```
tccli dc DescribePublicDirectConnectTunnelRoutes --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-6mqd6t9j
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "Status": "ENABLE",
                "DestinationCidrBlock": "10.19.166.0/24",
                "ASPath": [
                    "45090",
                    "58835"
                ],
                "RouteType": "STATIC",
                "RouteId": "dcxr-mtb4iw15",
                "NextHop": ""
            },
            {
                "Status": "ENABLE",
                "DestinationCidrBlock": "10.19.167.0/24",
                "ASPath": [
                    "45090",
                    "58835"
                ],
                "RouteType": "BGP",
                "RouteId": "dcxr-rjt3luud",
                "NextHop": ""
            },
            {
                "Status": "ENABLE",
                "DestinationCidrBlock": "10.19.168.0/24",
                "ASPath": [
                    "45090",
                    "58835"
                ],
                "RouteType": "BGP",
                "RouteId": "dcxr-eeinewg5",
                "NextHop": ""
            }
        ],
        "TotalCount": 3,
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea"
    }
}
```

