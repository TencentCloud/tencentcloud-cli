**Example 1: 修改路由信息**

修改上游服务名

Input: 

```
tccli tcb ModifyHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Domain.Domain xxx.***************.cn \
    --Domain.Routes.0.Path /api/v1 \
    --Domain.Routes.0.UpstreamResourceType CBR \
    --Domain.Routes.0.UpstreamResourceName my-service-new
```

Output: 
```
{
    "Response": {
        "RequestId": "3ebe9641-2c38-4ebd-b429-dc74ba74bcb7"
    }
}
```

