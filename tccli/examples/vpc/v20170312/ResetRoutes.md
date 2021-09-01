**Example 1: 重置路由表名称和路由策略**



Input: 

```
tccli vpc ResetRoutes --cli-unfold-argument  \
    --Version 2017-03-12 \
    --RouteTableId rtb-n0yejvje \
    --RouteTableName ResetRouteTableName \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription test-cvm-route
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

