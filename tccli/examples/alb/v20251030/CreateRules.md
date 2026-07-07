**Example 1: 创建规则**



Input: 

```
tccli alb CreateRules --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --ListenerId lst-d9p3k7wa \
    --Rules.0.Direction Request \
    --Rules.0.Priority 1 \
    --Rules.0.RuleName rule1 \
    --Rules.0.Conditions.0.Type Host \
    --Rules.0.Conditions.0.HostConfig test.com \
    --Rules.0.Actions.0.Type TargetGroup \
    --Rules.0.Actions.0.Order 1 \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroups.0.TargetGroupId lbtg-0zrnc9qa \
    --Rules.0.Actions.0.TargetGroupConfig.TargetGroups.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RuleIds": [
            "rule-h8cy5gwl"
        ],
        "RequestId": "d3614848-765c-4890-b381-72a192ac8c21"
    }
}
```

