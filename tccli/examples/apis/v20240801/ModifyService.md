**Example 1: 修改服务**



Input: 

```
tccli apis ModifyService --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Name copyofcopyofcopyofbbb \
    --PaasID app-be27914b \
    --Description test desc \
    --AuthType none \
    --SignType sha256 \
    --TargetSelect random \
    --PubPath /bbb \
    --RequestMethod any \
    --HttpProtocolType http \
    --CheckTargetCertsError False \
    --HttpProtocolVersion 1.1 \
    --TargetPath / \
    --RequestParamsValidatorStatus False \
    --RequestParamsValidatorJsonInfoT {"Body":{"Type":"object"},"Query":{"Type":"object"},"Header":{"Type":"object"}} \
    --ResponseParamsValidatorStatus False \
    --ResponseParamsValidatorJsonInfoT {"Body":{"Type":"object"},"Query":{"Type":"object"},"Header":{"Type":"object"}} \
    --InvokeLimitConfigStatus False \
    --InvokeLimitConfig.Type tokenBucket \
    --InvokeLimitConfig.TokenBucketMaxNum 20000 \
    --InvokeLimitConfig.TokenBucketRate 1 \
    --InvokeLimitConfig.FunnelMaxNum 20000 \
    --InvokeLimitConfig.FunnelRate 1 \
    --InvokeLimitConfig.SlidingWindowMaxNum 20000 \
    --InvokeLimitConfig.SlidingWindowSize 1 \
    --InvokeLimitConfig.TimeWindow 20000 \
    --InvokeLimitConfig.TimeWindowInterval 1 \
    --HealthCheckStatus False \
    --HealthCheckConfig.HealthCheckPath  \
    --HealthCheckConfig.ValidHealthCheckStatusCode 200 \
    --HealthCheckConfig.HealthCheckTimeout 0 \
    --SourceTypeStatus False \
    --SourceTypeConfig.ReqSourceType  \
    --SourceTypeConfig.ReqTargetType  \
    --SourceTypeConfig.ResSourceType  \
    --SourceTypeConfig.ResTargetType  \
    --IpWhiteStatus False \
    --IpBlackStatus False \
    --ID svr-b9027f2d
```

Output: 
```
{
    "Response": {
        "RequestId": "b9ed80fd-bdc8-428b-977a-32c7f0a0ca0c"
    }
}
```

