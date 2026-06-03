**Example 1: 创建完整路由**



Input: 

```
tccli tcb CreateHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Domain.Domain xxx.***************.cn \
    --Domain.AccessType DIRECT \
    --Domain.CertId *****3uC \
    --Domain.Protocol HTTP_AND_HTTPS \
    --Domain.CustomCname xxx.woyaodaguaishou.cn.eo.dns.com \
    --Domain.Enable True \
    --Domain.Routes.0.Path /api/v1 \
    --Domain.Routes.0.UpstreamResourceType CBR \
    --Domain.Routes.0.UpstreamResourceName my-service \
    --Domain.Routes.0.EnableSafeDomain False \
    --Domain.Routes.0.EnablePathTransmission False \
    --Domain.Routes.0.QPSPolicy.QPSTotal 100 \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitBy ClientIP \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitValue 10 \
    --Domain.Routes.0.Enable True \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Key X-Custom-Header \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Value custom-value \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Action OVERWRITE_IF_EXISTS_OR_ADD \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToRemove X-Remove-Me \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Key X-Response-Custom \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Value resp-value \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Action ADD_IF_ABSENT \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToRemove X-Resp-Remove \
    --Domain.Extension.HeadersHandler.RequestHeadersToAdd.0.Key X-Custom-Header \
    --Domain.Extension.HeadersHandler.RequestHeadersToAdd.0.Value custom-value \
    --Domain.Extension.HeadersHandler.RequestHeadersToAdd.0.Action OVERWRITE_IF_EXISTS_OR_ADD \
    --Domain.Extension.HeadersHandler.RequestHeadersToRemove X-Remove-Me \
    --Domain.Extension.HeadersHandler.ResponseHeadersToAdd.0.Key X-Response-Custom \
    --Domain.Extension.HeadersHandler.ResponseHeadersToAdd.0.Value resp-value \
    --Domain.Extension.HeadersHandler.ResponseHeadersToAdd.0.Action ADD_IF_ABSENT \
    --Domain.Extension.HeadersHandler.ResponseHeadersToRemove X-Resp-Remove
```

Output: 
```
{
    "Response": {
        "RequestId": "e9f7150d-e942-4c5b-a2df-b45b3db55e2a"
    }
}
```

