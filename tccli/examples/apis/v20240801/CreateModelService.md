**Example 1: CreateModelService**

CreateModelService

Input: 

```
tccli apis CreateModelService --cli-unfold-argument  \
    --InstanceID ins-******** \
    --Name deepseek \
    --Description deepseek \
    --PubPath /deepseek \
    --TargetModels.0.ID mod-******** \
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
    --PromptModerateConfig.InterceptMessage intercept
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mds-********"
        },
        "RequestId": "19539a7c-9462-4cd2-9064-0edaec692f17"
    }
}
```

