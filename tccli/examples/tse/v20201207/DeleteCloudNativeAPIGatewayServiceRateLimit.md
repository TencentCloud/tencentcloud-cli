**Example 1: 删除云原生网关限流插件(服务)**

删除云原生网关限流插件(服务)

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

