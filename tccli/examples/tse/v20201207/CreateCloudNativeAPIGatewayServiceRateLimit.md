**Example 1: 创建云原生网关限流插件(服务)**

创建云原生网关限流插件(服务)

Input: 

```
tccli tse CreateCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId gateway-dde037x1 \
    --Name 公网接入网关 \
    --LimitDetail.Enabled True \
    --LimitDetail.QpsThresholds.0.Unit second \
    --LimitDetail.QpsThresholds.0.Max 10 \
    --LimitDetail.Path /v1/users \
    --LimitDetail.Header X-Api-Version \
    --LimitDetail.LimitBy header \
    --LimitDetail.ExternalRedis.RedisHost 192.168.2.162 \
    --LimitDetail.ExternalRedis.RedisPassword tse@tencent \
    --LimitDetail.ExternalRedis.RedisPort 6379 \
    --LimitDetail.ExternalRedis.RedisTimeout 10 \
    --LimitDetail.Policy redis \
    --LimitDetail.RateLimitResponse.Body too many requests \
    --LimitDetail.RateLimitResponse.Headers.0.Key app \
    --LimitDetail.RateLimitResponse.Headers.0.Value kong \
    --LimitDetail.RateLimitResponse.HttpStatus 429 \
    --LimitDetail.RateLimitResponseUrl http://192.168.2.165/downgrade \
    --LimitDetail.ResponseType default \
    --LimitDetail.HideClientHeaders True \
    --LimitDetail.IsDelay True \
    --LimitDetail.LineUpTime 10
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

