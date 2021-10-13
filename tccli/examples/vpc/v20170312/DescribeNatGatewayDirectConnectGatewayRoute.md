**Example 1: 查NAT网关路由信息**



Input: 

```
tccli vpc DescribeNatGatewayDirectConnectGatewayRoute --cli-unfold-argument  \
    --NatGatewayId nat-2jd1e1rm \
    --VpcId vpc-3m6kvgrx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "NatDirectConnectGatewayRouteSet": [
            {
                "DestinationCidrBlock": "99.99.99.77/32",
                "UpdateTime": "2020-09-22 00:00:00",
                "GatewayType": "DIRECTCONNECT",
                "GatewayId": "dcg-71awizmv",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "852bd0e9-2104-4e83-b0fc-87c2c2036140"
    }
}
```

