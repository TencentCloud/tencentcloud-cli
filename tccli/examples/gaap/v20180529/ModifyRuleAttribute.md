**Example 1: 修改转发规则信息**



Input: 

```
tccli gaap ModifyRuleAttribute --cli-unfold-argument  \
    --RuleId rule-5g8dh58 \
    --HealthCheck 0 \
    --ListenerId listener-8fueuc9 \
    --CheckParams.Domain string \
    --CheckParams.ConnectTimeout 12 \
    --CheckParams.Path str \
    --CheckParams.Method string \
    --CheckParams.DelayLoop 1 \
    --CheckParams.StatusCode 1 \
    --Scheduler rr \
    --Path /
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

