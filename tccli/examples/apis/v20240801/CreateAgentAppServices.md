**Example 1: 关联应用与服务**



Input: 

```
tccli apis CreateAgentAppServices --cli-unfold-argument  \
    --InstanceID ins-222fd0da \
    --ID aga-cc2448c0 \
    --Services.0.ID svr-17244a65 \
    --Services.0.InvokeLimitConfigStatus False \
    --Services.0.InvokeLimitConfig.Type tokenBucket \
    --Services.0.InvokeLimitConfig.TokenBucketMaxNum 100 \
    --Services.0.InvokeLimitConfig.TokenBucketRate 6 \
    --Services.0.InvokeLimitConfig.FunnelMaxNum 122 \
    --Services.0.InvokeLimitConfig.FunnelRate 122 \
    --Services.0.InvokeLimitConfig.SlidingWindowMaxNum 1212 \
    --Services.0.InvokeLimitConfig.SlidingWindowSize 12 \
    --Services.0.InvokeLimitConfig.TimeWindow 12 \
    --Services.0.InvokeLimitConfig.TimeWindowInterval 12 \
    --Services.0.InvokeLimitConfig.Timeout 212 \
    --Services.0.NeedAuth True \
    --Services.0.AgentCredentialID agc-aca72fd4
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-cc2448c0"
        },
        "RequestId": "fb28b7e3-0b0a-4303-9ac9-29dbbaef7b7f"
    }
}
```

