**Example 1: 修改七层转发规则**



Input: 

```
tccli ga2 ModifyForwardingRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h \
    --ForwardingPolicyId dm-kzk3neks \
    --ForwardingRuleId rule-5lybgwaw \
    --RuleConditions.0.RuleConditionType Path \
    --RuleConditions.0.RuleConditionValue \cc
```

Output: 
```
{
    "Response": {
        "RequestId": "e6437f6a-18e9-4a61-895b-28d5083297f4",
        "TaskId": "2347cd92-de71-40d9-a6b4-eeee09a14513"
    }
}
```

