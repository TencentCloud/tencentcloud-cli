**Example 1: 创建限流规则**



Input: 

```
tccli waf CreateRateLimitV2 --cli-unfold-argument  \
    --Domain www.test.com \
    --Name testName \
    --Priority 0 \
    --Status 0 \
    --LimitMethod.Method GET \
    --LimitMethod.Type EXACT \
    --LimitPaths.Path /testurl \
    --LimitPaths.Type EXACT \
    --LimitHeaders.0.Key name \
    --LimitHeaders.0.Value waf_value \
    --LimitHeaders.0.Type EXACT \
    --LimitWindow.Second 0 \
    --LimitWindow.Minute 10 \
    --LimitHeaderName.ParamsName name \
    --LimitHeaderName.Type EXACT \
    --LimitObject API \
    --LimitStrategy 0
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "Code": 1,
            "Info": "success"
        },
        "RequestId": "546b2091-1a59-4bd9-818d-47ab565102d9"
    }
}
```

