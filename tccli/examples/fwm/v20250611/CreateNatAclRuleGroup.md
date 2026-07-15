**Example 1: 创建NAT 规则组**



Input: 

```
tccli fwm CreateNatAclRuleGroup --cli-unfold-argument  \
    --GroupName one \
    --Product cfw_nat_acl \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 0.0.0.0/0 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope ap-shanghai \
    --Rules.0.Direction 1 \
    --Rules.0.Port -1/-1 \
    --Rules.0.Description zero \
    --Rules.0.ParamTemplateId  \
    --Rules.1.SourceContent 0.0.0.0/0 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 0.0.0.0/0 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol UDP \
    --Rules.1.RuleAction accept \
    --Rules.1.OrderIndex 2 \
    --Rules.1.Scope cfwnat-e7ad7c24 \
    --Rules.1.Direction 1 \
    --Rules.1.Port -1/-1 \
    --Rules.1.Description 222 \
    --Rules.1.ParamTemplateId  \
    --Rules.1.BelongMemberId 1300448058 \
    --Rules.2.SourceContent 0.0.0.0/0 \
    --Rules.2.SourceType net \
    --Rules.2.TargetContent 0.0.0.0/0 \
    --Rules.2.TargetType net \
    --Rules.2.Protocol ANY \
    --Rules.2.RuleAction accept \
    --Rules.2.OrderIndex 3 \
    --Rules.2.Scope ALL \
    --Rules.2.Direction 1 \
    --Rules.2.Port -1/-1 \
    --Rules.2.Description 333 \
    --Rules.2.ParamTemplateId 
```

Output: 
```
{
    "Response": {
        "GroupId": "fwmrg_wrzekq94u7",
        "RequestId": "62cbbbe0-bac7-4e18-a85c-94a7784dfd04"
    }
}
```

