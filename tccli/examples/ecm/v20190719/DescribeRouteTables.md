**Example 1: 查看路由表对象列表**



Input: 

```
tccli ecm DescribeRouteTables --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-2at5y1pn",
                "RouteTableId": "rtb-l2h8d7c2",
                "RouteTableName": "demo",
                "AssociationSet": [],
                "RouteSet": [
                    {
                        "RouteItemId": "rti-ms7c7gcr",
                        "RouteId": 0,
                        "RouteTableId": "rtb-l2h8d7c2",
                        "DestinationCidrBlock": "169.254.64.0/23",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.25",
                        "RouteType": "USER",
                        "RouteDescription": "demo",
                        "Enabled": true
                    }
                ],
                "Main": false,
                "CreatedTime": "2020-11-30 19:52:03"
            }
        ],
        "TotalCount": 2,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

