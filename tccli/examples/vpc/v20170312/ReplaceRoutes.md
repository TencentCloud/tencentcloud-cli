**Example 1: 替换路由策略**

替换路由策略

Input: 

```
tccli vpc ReplaceRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.RouteItemId rti-hj3he929 \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription demo \
    --Routes.0.Enabled True \
    --Routes.0.PublishedToVbc True
```

Output: 
```
{
    "Response": {
        "NewRouteSet": [
            {
                "RouteTableId": "rtb-n0yejvje",
                "RouteId": 10262,
                "RouteItemId": "rti-hj3he929",
                "RouteType": "USER",
                "DestinationCidrBlock": "192.168.0.0/16",
                "DestinationIpv6CidrBlock": "",
                "RouteDescription": "demo",
                "GatewayType": "NORMAL_CVM",
                "GatewayId": "172.16.16.37",
                "Enabled": true,
                "PublishedToVbc": true,
                "CreatedTime": "2018-10-10 17:10:09"
            }
        ],
        "OldRouteSet": [
            {
                "RouteTableId": "rtb-n0yejvje",
                "RouteId": 10262,
                "RouteItemId": "rti-hj3he929",
                "RouteType": "USER",
                "DestinationCidrBlock": "172.16.1.0/24",
                "DestinationIpv6CidrBlock": "",
                "RouteDescription": "",
                "GatewayType": "NORMAL_CVM",
                "GatewayId": "10.0.0.10",
                "Enabled": true,
                "PublishedToVbc": true,
                "CreatedTime": "2018-10-10 17:03:09"
            }
        ],
        "RequestId": "3f934a21-2786-44af-a421-38ee6c6e1fae"
    }
}
```

