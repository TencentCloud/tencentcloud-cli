**Example 1: 创建互联网边界规则组**



Input: 

```
tccli fwm CreateEdgeAclRuleGroup --cli-unfold-argument  \
    --GroupName edge \
    --Product cfw_edge_acl \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Direction 1 \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 0.0.0.0/0 \
    --Rules.0.TargetType net \
    --Rules.0.Port -1/-1 \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Description 1212 \
    --Rules.0.Scope all \
    --Rules.1.OrderIndex 2 \
    --Rules.1.Direction 1 \
    --Rules.1.SourceContent bj11 \
    --Rules.1.SourceType location \
    --Rules.1.TargetContent cfwnat-e366d270 \
    --Rules.1.TargetType instance \
    --Rules.1.Port -1/-1 \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction accept \
    --Rules.1.Description 3232 \
    --Rules.1.Scope all \
    --Rules.1.BelongMemberId 1300448058
```

Output: 
```
{
    "Response": {
        "GroupId": "fwmrg_4ae6vv1l7c",
        "RequestId": "fcb93770-4c26-4b35-9ded-8daec5b99a19"
    }
}
```

