**Example 1: 添加规则**

往已存在的规则组添加规则

Input: 

```
tccli fwm CreateSecurityGroupRule --cli-unfold-argument  \
    --GroupId fwmrg-9cbtdqxxxe \
    --Rules.0.IpVersion ipv4 \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 0.0.0.0/0 \
    --Rules.0.DestType net \
    --Rules.0.Protocol ANY \
    --Rules.0.Port -1/-1 \
    --Rules.0.ServiceTemplateId  \
    --Rules.0.RuleAction accept \
    --Rules.0.Description 1212 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope SG \
    --Rules.0.ProtocolPortType 0
```

Output: 
```
{
    "Response": {
        "RuleIds": [
            "00b4416a-efd3-4326-a19c-c1c333184e05"
        ],
        "RequestId": "fcdd5c06-b16e-4101-bfff-03e973e70081"
    }
}
```

