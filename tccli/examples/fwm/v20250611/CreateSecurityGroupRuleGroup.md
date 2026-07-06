**Example 1: 创建规则组**



Input: 

```
tccli fwm CreateSecurityGroupRuleGroup --cli-unfold-argument  \
    --GroupName 归属测试组1 \
    --Product enterprise_sg \
    --Rules.0.IpVersion ipv4 \
    --Rules.0.SourceContent subnet-imemp5hz \
    --Rules.0.SourceType instance \
    --Rules.0.DestContent 0.0.0.0/0 \
    --Rules.0.DestType net \
    --Rules.0.Protocol ANY \
    --Rules.0.Port -1/-1 \
    --Rules.0.ServiceTemplateId  \
    --Rules.0.RuleAction accept \
    --Rules.0.Description 1221 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope SG \
    --Rules.0.ProtocolPortType 0 \
    --Rules.0.BelongMemberId 1302477603 \
    --Rules.1.IpVersion ipv4 \
    --Rules.1.SourceContent 192.168.0.0/16 \
    --Rules.1.SourceType net \
    --Rules.1.DestContent 0.0.0.0/0 \
    --Rules.1.DestType net \
    --Rules.1.Protocol ANY \
    --Rules.1.Port -1/-1 \
    --Rules.1.ServiceTemplateId  \
    --Rules.1.RuleAction accept \
    --Rules.1.Description 33333 \
    --Rules.1.OrderIndex 2 \
    --Rules.1.Scope SG \
    --Rules.1.ProtocolPortType 0
```

Output: 
```
{
    "Response": {
        "GroupId": "fwmrg-jvw5ulal",
        "RequestId": "1af65155-debe-49ca-b9d3-cac479b51cc7"
    }
}
```

