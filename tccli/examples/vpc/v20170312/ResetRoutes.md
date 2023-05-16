**Example 1: 重置路由表名称和路由策略**

重置路由表名称和路由策略

Input: 

```
tccli vpc ResetRoutes --cli-unfold-argument  \
    --RouteTableId rtb-n0yejvje \
    --RouteTableName TEST \
    --Routes.0.RouteId 1 \
    --Routes.0.DestinationCidrBlock 192.168.0.0/16 \
    --Routes.0.GatewayType NORMAL_CVM \
    --Routes.0.GatewayId 172.16.16.37 \
    --Routes.0.RouteDescription abc \
    --Routes.0.Enabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

