**Example 1: ModifyModelService**

ModifyModelService

Input: 

```
tccli apis ModifyModelService --cli-unfold-argument  \
    --InstanceID ins-******** \
    --ID mds-******** \
    --Name deepseek \
    --Description deepseek \
    --TargetModels.0.ID mod-78bd8b5e \
    --TargetModels.0.Name deepseek \
    --TargetModels.0.Rank 10 \
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
    --IpBlackStatus False \
    --Timeout 60 \
    --PromptModerateStatus False \
    --PromptModerateConfig.Action watch \
    --PromptModerateConfig.InterceptMessage 
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mds-********"
        },
        "RequestId": "ebd06dc9-30ae-4f30-84eb-a1ed61d7a098"
    }
}
```

