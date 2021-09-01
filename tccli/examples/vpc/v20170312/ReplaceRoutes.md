**Example 1: 替换路由策略**



Input: 

```
tccli vpc ReplaceRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.RouteId 17125 \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription leo-test-CVM-route
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
                "GatewayType": "PEERCONNECTION",
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

