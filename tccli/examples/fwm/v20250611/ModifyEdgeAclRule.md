**Example 1: 修改互联网边界规则**



Input: 

```
tccli fwm ModifyEdgeAclRule --cli-unfold-argument  \
    --GroupId fwmrg_4ae6vv1l7c \
    --Rule.RuleId fb65eefd-6a64-4c02-a720-e278d41df8bd \
    --Rule.OrderIndex 3 \
    --Rule.Direction 1 \
    --Rule.SourceContent 0.0.0.0/0 \
    --Rule.SourceType net \
    --Rule.TargetContent 0.0.0.0/0 \
    --Rule.TargetType net \
    --Rule.Port -1/-1 \
    --Rule.Protocol TCP \
    --Rule.RuleAction drop \
    --Rule.Description 77777 \
    --Rule.Scope all
```

Output: 
```
{
    "Response": {
        "RequestId": "6664b107-391d-473d-a59a-88502841fa0e"
    }
}
```

