**Example 1: 云原生网关创建限流插件(路由)**

云原生网关创建限流插件(路由)

Input: 

```
tccli tse CreateCloudNativeAPIGatewayRouteRateLimit --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Id 6f423439-ec27-4a2e-aff9-9e73ffa3da4d \
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
        "RequestId": "3124124141241fas432"
    }
}
```

