**Example 1: 删除云原生网关限流插件(路由)**

删除云原生网关限流插件(路由)

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId abc \
    --Id abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

