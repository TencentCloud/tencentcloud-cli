**Example 1: 删除路由表的路由规则**

删除路由表的路由,支持IPv4,IPv6路由删除

Input: 

```
tccli vpc DeleteRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.RouteId 1 \
    --Routes.0.DestinationCidrBlock 192.241.0.0/24 \
    --Routes.0.GatewayType EIP \
    --Routes.0.GatewayId vpc-pymolayx \
    --Routes.0.RouteDescription TEST \
    --Routes.0.Enabled True \
    --Routes.0.RouteType USER \
    --Routes.0.RouteTableId rtb-n0yejvje \
    --Routes.0.DestinationIpv6CidrBlock 201::/16 \
    --Routes.0.RouteItemId rti-pbta2ruf \
    --Routes.0.PublishedToVbc True \
    --Routes.0.CreatedTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": 1,
                "DestinationCidrBlock": "192.241.0.0/24",
                "GatewayType": "EIP",
                "GatewayId": "vpc-pymolayx",
                "RouteDescription": "TEST",
                "Enabled": true,
                "RouteType": "USER",
                "RouteTableId": "rtb-n0yejvje",
                "DestinationIpv6CidrBlock": "201::/16",
                "RouteItemId": "rti-pbta2ruf",
                "PublishedToVbc": true,
                "CreatedTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "10098418-f013-4d3e-855b-e086f0544b44"
    }
}
```

