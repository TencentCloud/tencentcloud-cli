**Example 1: 修改云原生网关限流插件(服务)**

修改云原生网关限流插件(服务)

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc \
    --LimitDetail.Enabled True \
    --LimitDetail.QpsThresholds.0.Unit second \
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
    --LimitDetail.LineUpTime 0 \
    --LimitDetail.IsDelay True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

