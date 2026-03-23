**Example 1: 修改mcp server**

修改mcp server

Input: 

```
tccli apis ModifyMcpServer --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --ID mcp-aa12c447 \
    --Mode proxy \
    --McpVersion 2024-11-05 \
    --Name testmcp \
    --Description  \
    --TargetSelect random \
    --TargetHosts.0.Host 127.0.0.1:3000 \
    --TargetHosts.0.Rank 10 \
    --HttpProtocolType http \
    --CheckTargetCertsError False \
    --TargetPath /sse \
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
    --IpWhiteStatus False \
    --IpWhiteConfig.EffectType always \
    --IpWhiteConfig.Comment  \
    --IpBlackStatus False \
    --IpBlackConfig.EffectType always \
    --IpBlackConfig.Comment  \
    --CustomHttpHost  \
    --HttpHostType targetHost \
    --Timeout 60 \
    --McpSecurityRules.0.ID mr-2bdbbf32 \
    --McpSecurityRules.0.Act watch \
    --McpSecurityRules.0.Status open
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mcp-aa12c447"
        },
        "RequestId": "388289da-01b2-4be6-8ba9-7b40028ac05b"
    }
}
```

