**Example 1: 创建路由规则**



Input: 

```
tccli vpc CreateRoutes --cli-unfold-argument  \
    --Version 2017-03-12\
    --RouteTableId rtb-n0yejvje\
    --Routes.0.DestinationCidrBlock 192.168.0.0/16\
    --Routes.0.GatewayType NORMAL_CVM\
    --Routes.0.GatewayId 172.16.16.37\
    --Routes.0.RouteDescription TEST-CVM-ROUTE
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
                        "RouteId": 12345678
                    }
                ],
                "Main": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "3f934a21-2786-44af-a421-38ee6c6e1fae"
    }
}
```

