**Example 1: 查看容器托管的所有服务**



Input: 

```
tccli tcb DescribeWxGatewayRoutes --cli-unfold-argument  \
    --GatewayId gatewayid-xxx \
    --EnvId envid-xxx \
    --GatewayVersion version-xxx \
    --GatewayRouteName route-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6b740e66-04dc-4389-808a-b496e70e7549",
        "TotalCount": 3,
        "WxGatewayRouteSet": [
            {
                "CustomHeader": {
                    "RequestToAddList": []
                },
                "FrequencyLimitConfig": [],
                "GatewayRewriteHost": "43.135.114.125",
                "GatewayRouteAddr": "access.xxie.site",
                "GatewayRouteClusterId": "access",
                "GatewayRouteCreateTime": "2024-11-19 10:37:49",
                "GatewayRouteDesc": "",
                "GatewayRouteEnvId": "",
                "GatewayRouteMethod": "ALL",
                "GatewayRouteName": "access",
                "GatewayRoutePath": "/test",
                "GatewayRoutePathMatchType": "prefix",
                "GatewayRoutePort": 0,
                "GatewayRouteProtocol": "http",
                "GatewayRouteServerName": "",
                "GatewayRouteServerType": "ip",
                "GatewayVersion": "version-xxx"
            }
        ]
    }
}
```

