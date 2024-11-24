**Example 1: 删除云原生网关限流插件(服务)**

删除云原生网关限流插件(服务)

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Name user-service
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

