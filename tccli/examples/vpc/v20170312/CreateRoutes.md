**Example 1: 创建路由规则**

创建路由规则

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
                        "DestinationCidrBlock": "192.168.0.0/16",
                        "RouteTableId": "rtb-n0yejvje",
                        "RouteItemId": "rti-psm73tvu",
                        "RouteDescription": "erty",
                        "Enabled": true,
                        "RouteId": 1,
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.16.37"
                    }
                ],
                "RouteTableId": "rtb-n0yejvje",
                "VpcId": "vpc-4cugx77a",
                "RouteTableName": "TEST",
                "TagSet": [
                    {
                        "Value": "test",
                        "Key": "ee"
                    }
                ],
                "CreatedTime": "2020-09-22 00:00:00",
                "AssociationSet": [
                    {
                        "SubnetId": "subnet-1234derf",
                        "RouteTableId": "rtb-n0yejvje"
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
        "RequestId": "a949ecd8-a223-4b96-8537-a8a68a5ba47a"
    }
}
```

