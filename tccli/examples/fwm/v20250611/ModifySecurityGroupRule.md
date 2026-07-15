**Example 1: 修改规则组内规则**



Input: 

```
tccli fwm ModifySecurityGroupRule --cli-unfold-argument  \
    --GroupId fwmrg-jvw5ulal \
    --Rule.IpVersion ipv4 \
    --Rule.SourceContent ins-3nav5p56 \
    --Rule.SourceType instance \
    --Rule.DestContent 0.0.0.0/0 \
    --Rule.DestType net \
    --Rule.Protocol ANY \
    --Rule.Port -1/-1 \
    --Rule.ServiceTemplateId  \
    --Rule.RuleAction accept \
    --Rule.Description 33333333 \
    --Rule.OrderIndex 1 \
    --Rule.RuleId 7394c937-85f9-4b0f-a30f-494d8369e4bd \
    --Rule.Scope SG \
    --Rule.ProtocolPortType 0 \
    --Rule.BelongMemberId 1302477603
```

Output: 
```
{
    "Response": {
        "RequestId": "dc7591e4-8fc8-417d-b355-07e7df3e8a19"
    }
}
```

