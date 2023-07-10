**Example 1: 修改云原生网关路由**

修改云原生网关路由

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayRoute --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --ServiceID 104dd157-5008-4d3c-9feb-4767667863ff \
    --RouteName route-demo \
    --RouteID 916462a4-8ce4-4605-a7b7-66cd51c38201 \
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

