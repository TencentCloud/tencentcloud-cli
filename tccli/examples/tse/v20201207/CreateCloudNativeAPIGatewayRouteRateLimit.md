**Example 1: 云原生网关创建限流插件(路由)**

云原生网关创建限流插件(路由)

Input: 

```
tccli tse CreateCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Id 5836e46f-1653-4183-a76e-c361540d0831 \
    --LimitDetail.Enabled True \
    --LimitDetail.QpsThresholds.0.Max 20 \
    --LimitDetail.QpsThresholds.0.Unit second \
    --LimitDetail.LimitBy consumer \
    --LimitDetail.Policy local \
    --LimitDetail.RateLimitResponse.HttpStatus 200 \
    --LimitDetail.ResponseType text \
    --LimitDetail.HideClientHeaders True \
    --LimitDetail.LineUpTime 1 \
    --LimitDetail.IsDelay True
```

Output: 
```
{
    "Response": {
        "RequestId": "552cae66-953b-490c-b2d7-4c7c8d1cbd05"
    }
}
```

