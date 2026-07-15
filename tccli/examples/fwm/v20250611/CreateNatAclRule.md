**Example 1:  添加 NAT 规则**



Input: 

```
tccli fwm CreateNatAclRule --cli-unfold-argument  \
    --GroupId fwmrg_go7u11gs6v \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 0.0.0.0/0 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol UDP \
    --Rules.0.RuleAction accept \
    --Rules.0.OrderIndex 2 \
    --Rules.0.Scope cfwnat-e7ad7c24 \
    --Rules.0.Direction 1 \
    --Rules.0.Port -1/-1 \
    --Rules.0.Description 444 \
    --Rules.0.ParamTemplateId  \
    --Rules.0.BelongMemberId 1300448058 \
    --Rules.1.SourceContent 0.0.0.0/0 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 0.0.0.0/0 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol ANY \
    --Rules.1.RuleAction accept \
    --Rules.1.OrderIndex 3 \
    --Rules.1.Scope ALL \
    --Rules.1.Direction 1 \
    --Rules.1.Port -1/-1 \
    --Rules.1.Description 555 \
    --Rules.1.ParamTemplateId  \
    --Rules.2.SourceContent 0.0.0.0/0 \
    --Rules.2.SourceType net \
    --Rules.2.TargetContent 0.0.0.0/0 \
    --Rules.2.TargetType net \
    --Rules.2.Protocol ANY \
    --Rules.2.RuleAction accept \
    --Rules.2.OrderIndex 1 \
    --Rules.2.Scope ALL \
    --Rules.2.Direction 0 \
    --Rules.2.Port -1/-1 \
    --Rules.2.Description 222 \
    --Rules.2.ParamTemplateId 
```

Output: 
```
{
    "Response": {
        "RequestId": "3deaf1ac-6319-4eb6-a989-0b9a13054616"
    }
}
```

