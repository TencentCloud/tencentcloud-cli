**Example 1: 修改转发规则信息**



Input: 

```
tccli gaap ModifyRuleAttribute --cli-unfold-argument  \
    --RuleId rule-5g8dh58 \
    --ListenerId listener-8fueuc9 \
    --Path / \
    --Scheduler rr \
    --HealthCheck 0 \
    --CheckParams.DelayLoop 1 \
    --CheckParams.Path str \
    --CheckParams.ConnectTimeout 12 \
    --CheckParams.StatusCode 1 \
    --CheckParams.Method string \
    --CheckParams.Domain string
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

