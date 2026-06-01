**Example 1: 创建七层转发规则**



Input: 

```
tccli ga2 CreateForwardingRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h \
    --ForwardingPolicyId dm-kzk3neks \
    --RuleConditions.0.RuleConditionType Path \
    --RuleConditions.0.RuleConditionValue /a \
    --RuleActions.0.RuleActionType Drop \
    --OriginHeaders.0.Key key-123 \
    --OriginHeaders.0.Value value-123 \
    --EnableOriginSni True \
    --OriginSni 123 \
    --OriginHost www.bbb.com
```

Output: 
```
{
    "Response": {
        "RequestId": "f7be96f3-c499-4efe-badd-0178c2921d8f",
        "TaskId": "6fa13601-49eb-4982-abee-513fbab41fc1",
        "ForwardingRuleId": "rule-kfn3oc78"
    }
}
```

