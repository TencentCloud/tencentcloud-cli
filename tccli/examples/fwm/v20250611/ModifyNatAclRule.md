**Example 1: 修改 NAT 规则**



Input: 

```
tccli fwm ModifyNatAclRule --cli-unfold-argument  \
    --GroupId fwmrg_go7u11gs6v \
    --Rule.SourceContent 0.0.0.0/0 \
    --Rule.SourceType net \
    --Rule.TargetContent 0.0.0.0/0 \
    --Rule.TargetType net \
    --Rule.Protocol UDP \
    --Rule.RuleAction accept \
    --Rule.OrderIndex 2 \
    --Rule.Scope cfwnat-e366d270 \
    --Rule.Direction 1 \
    --Rule.RuleId 5712589f-c85c-4b3e-8917-bc3bb5779133 \
    --Rule.Port -1/-1 \
    --Rule.Description 444 \
    --Rule.ParamTemplateId  \
    --Rule.BelongMemberId 1300448058
```

Output: 
```
{
    "Response": {
        "RequestId": "1b4f862f-f14a-47e9-8d4d-9ff400989ed4"
    }
}
```

