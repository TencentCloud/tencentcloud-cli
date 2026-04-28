**Example 1: CreateModelService**

CreateModelService

Input: 

```
tccli apis CreateModelService --cli-unfold-argument  \
    --InstanceID ins-******** \
    --Name testmodel \
    --Description testmodel \
    --PubPath /model \
    --TargetModels.0.ID ins-******** \
    --TargetModels.0.Name deepseek \
    --TargetModels.0.Rank 10 \
    --PathMatchType prefix \
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
    --InvokeLimitConfig.Timeout 60 \
    --TokenLimitStatus False \
    --TokenLimitConfig.LimitRequestBody 10 \
    --TokenLimitConfig.LimitWindows.0.Interval 60 \
    --TokenLimitConfig.LimitWindows.0.Limit 100 \
    --TmsStatus False \
    --TmsConfig.Mode  \
    --TmsConfig.Action  \
    --TmsConfig.MergeCount 0 \
    --TmsConfig.BizType  \
    --TmsConfig.InterceptMessage  \
    --IpWhiteStatus False \
    --Timeout 60 \
    --PromptModerateStatus True \
    --PromptModerateConfig.Action intercept \
    --PromptModerateConfig.InterceptMessage intercept \
    --TargetSelect consistentHash \
    --FindHostKeyMethod autoDetect \
    --HostKeyHeaderName x-session-id \
    --FallbackStatus False
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mds-572bf562"
        },
        "RequestId": "3766ec52-78e1-478a-a83d-686981c94a92"
    }
}
```

