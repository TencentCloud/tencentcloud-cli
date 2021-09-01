**Example 1: 创建路由规则**



Input: 

```
tccli vpc CreateRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription TEST-CVM-ROUTE
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RouteTableSet": [
            {
                "RouteSet": [
                    {
                        "CreatedTime": "2020-09-22 00:00:00",
                        "DestinationCidrBlock": "10.0.0.0/24",
                        "RouteTableId": "rtb-1234derf",
                        "RouteItemId": "xx",
                        "RouteDescription": "erty",
                        "Enabled": true,
                        "RouteId": 1,
                        "GatewayType": "xx",
                        "PublishedToVbc": true,
                        "GatewayId": "xx",
                        "DestinationIpv6CidrBlock": "xx",
                        "RouteType": "xx"
                    }
                ],
                "RouteTableId": "xx",
                "VpcId": "xx",
                "RouteTableName": "xx",
                "TagSet": [
                    {
                        "Value": "test",
                        "Key": "ee"
                    }
                ],
                "CreatedTime": "2020-09-22 00:00:00",
                "AssociationSet": [
                    {
                        "SubnetId": "xx",
                        "RouteTableId": "xx"
                    }
                ],
                "Main": false,
                "LocalCidrForCcn": [
                    {
                        "Cidr": "10.0.0.0/16",
                        "PublishedToVbc": true
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

