**Example 1: 创建完整路由**



Input: 

```
tccli tcb CreateHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Domain.Domain xxx.***************.cn \
    --Domain.AccessType DIRECT \
    --Domain.CertId VF****** \
    --Domain.Protocol HTTP_AND_HTTPS \
    --Domain.CustomCname xxx.*********************.dns.com \
    --Domain.Enable True \
    --Domain.Routes.0.Path /api/v1 \
    --Domain.Routes.0.UpstreamResourceType CBR \
    --Domain.Routes.0.UpstreamResourceName my-service \
    --Domain.Routes.0.EnableSafeDomain False \
    --Domain.Routes.0.EnablePathTransmission False \
    --Domain.Routes.0.QPSPolicy.QPSTotal 100 \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitBy ClientIP \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitValue 10 \
    --Domain.Routes.0.Enable True
```

Output: 
```
{
    "Response": {
        "RequestId": "424af1fa-ea4d-4a63-b96c-b374d5dfb020"
    }
}
```

