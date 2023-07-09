**Example 1: 创建云原生网关路由**

创建云原生网关路由

Input: 

```
tccli tse CreateCloudNativeAPIGatewayRoute --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --ServiceID service-demo \
    --RouteName route-demo \
    --Methods GET POST \
    --Hosts www.baidu.com \
    --Paths / \
    --PreserveHost True \
    --StripPath False \
    --HttpsRedirectStatusCode 308
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

