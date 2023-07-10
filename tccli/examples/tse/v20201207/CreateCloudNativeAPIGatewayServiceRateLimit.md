**Example 1: 创建云原生网关限流插件(服务)**

创建云原生网关限流插件(服务)

Input: 

```
tccli tse CreateCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc \
    --LimitDetail.Enabled True \
    --LimitDetail.QpsThresholds.0.Unit abc \
    --LimitDetail.QpsThresholds.0.Max 10 \
    --LimitDetail.Path abc \
    --LimitDetail.Header abc \
    --LimitDetail.LimitBy abc \
    --LimitDetail.ExternalRedis.RedisHost abc \
    --LimitDetail.ExternalRedis.RedisPassword abc \
    --LimitDetail.ExternalRedis.RedisPort 0 \
    --LimitDetail.ExternalRedis.RedisTimeout 0 \
    --LimitDetail.Policy abc \
    --LimitDetail.RateLimitResponse.Body abc \
    --LimitDetail.RateLimitResponse.Headers.0.Key abc \
    --LimitDetail.RateLimitResponse.Headers.0.Value abc \
    --LimitDetail.RateLimitResponse.HttpStatus 0 \
    --LimitDetail.RateLimitResponseUrl abc \
    --LimitDetail.ResponseType abc \
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

