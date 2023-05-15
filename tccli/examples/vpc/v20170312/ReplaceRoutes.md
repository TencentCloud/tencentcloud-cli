**Example 1: 替换路由策略**

替换路由策略

Input: 

```
tccli vpc ReplaceRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.RouteId 17125 \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription abc \
    --Routes.0.Enabled True \
    --Routes.0.RouteType abc \
    --Routes.0.RouteTableId abc \
    --Routes.0.DestinationIpv6CidrBlock abc \
    --Routes.0.RouteItemId abc \
    --Routes.0.PublishedToVbc True \
    --Routes.0.CreatedTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "NewRouteSet": [
            {
                "DestinationCidrBlock": "172.16.16.37/22",
                "RouteTableId": "rtb-n0yejvje",
                "RouteDescription": "",
                "GatewayType": "NORMAL_CVM",
                "GatewayId": "pcx-n9vkqrtm"
            }
        ],
        "RequestId": "3f934a21-2786-44af-a421-38ee6c6e1fae",
        "OldRouteSet": [
            {
                "DestinationCidrBlock": "172.16.16.37/21",
                "RouteTableId": "rtb-n0yejvje",
                "RouteDescription": "",
                "GatewayType": "PEERCONNECTION",
                "GatewayId": "pcx-n9vkqrtk"
            }
        ]
    }
}
```

