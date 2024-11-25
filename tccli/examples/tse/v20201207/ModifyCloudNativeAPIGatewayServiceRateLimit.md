**Example 1: 修改云原生网关限流插件(服务)**

修改云原生网关限流插件(服务)

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayServiceRateLimit --cli-unfold-argument  \
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
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

