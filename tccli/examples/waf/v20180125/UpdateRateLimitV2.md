**Example 1: 更新限流规则**



Input: 

```
tccli waf UpdateRateLimitV2 --cli-unfold-argument  \
    --Domain www.test.com \
    --LimitRuleId 0 \
    --Name testname \
    --Priority 0 \
    --Status 0 \
    --LimitMethod.Method GET \
    --LimitMethod.Type EXACT \
    --LimitPaths.Path /testurl \
    --LimitPaths.Type EXACT \
    --LimitHeaders.0.Key key_a \
    --LimitHeaders.0.Value value_a,value_b \
    --LimitHeaders.0.Type IN \
    --LimitWindow.Second 0 \
    --LimitWindow.Minute 10 \
    --LimitHeaderName.ParamsName keya,keyb \
    --LimitHeaderName.Type IN \
    --LimitObject API \
    --LimitStrategy 0
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "Code": 0,
            "Info": "success"
        },
        "RequestId": "546b2091-1a59-4bd9-818d-47ab565102d9"
    }
}
```

