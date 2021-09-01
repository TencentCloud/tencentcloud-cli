**Example 1: 创建路由策略**



Input: 

```
tccli ecm CreateRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 10.212.0.13 \
    --Routes.0.RouteDescription TEST-ROUTE
```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-k23blx7p",
                "RouteTableId": "rtb-n0yejvje",
                "RouteTableName": "TestRoutes",
                "AssociationSet": [],
                "RouteSet": [
                    {
                        "RouteItemId": "rti-12345678",
                        "DestinationCidrBlock": "192.168.0.0/16",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "10.212.0.13",
                        "RouteDescription": "TEST-ROUTE"
                    }
                ],
                "Main": false,
                "CreatedTime": "2020-11-11 11:11:03"
            }
        ],
        "TotalCount": 1,
        "RequestId": "3f934a21-2786-44af-a421-38ee6c6e1fae"
    }
}
```

