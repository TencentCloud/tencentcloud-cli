**Example 1: 查看容器托管的所有服务**



Input: 

```
tccli tcb DescribeWxGatewayRoutes --cli-unfold-argument  \
    --GatewayId xx \
    --EnvId xx \
    --GatewayVersion xx \
    --GatewayRouteName xx
```

Output: 
```
{
    "Response": {
        "WxGatewayRouteSet": [
            {
                "GatewayRouteAddr": "xx",
                "GatewayRouteDesc": "xx",
                "GatewayRouteProtocol": "xx",
                "GatewayRouteName": "xx",
                "GatewayVersion": "xx"
            }
        ],
        "TotalCount": 10,
        "RequestId": "xx"
    }
}
```

