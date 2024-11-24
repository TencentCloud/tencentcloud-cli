**Example 1: 删除云原生网关限流插件(路由)**

删除云原生网关限流插件(路由)

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Id 2a212560-220a-46f6-b139-3238eb8ea041
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

