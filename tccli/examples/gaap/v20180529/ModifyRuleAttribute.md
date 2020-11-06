**Example 1: 修改转发规则信息**



Input: 

```
tccli gaap ModifyRuleAttribute --cli-unfold-argument  \
    --RuleId rule-5g8dh58 \
    --ListenerId listener-8fueuc9 \
    --Path / \
    --Scheduler rr \
    --HealthCheck 0 \
    --CheckParam null
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

