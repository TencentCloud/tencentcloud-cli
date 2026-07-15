**Example 1: 创建 vpc 规则组**



Input: 

```
tccli fwm CreateVpcAclRuleGroup --cli-unfold-argument  \
    --GroupName 222 \
    --Product cfw_vpc_acl \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 0.0.0.0/0 \
    --Rules.0.DestType net \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction accept \
    --Rules.0.OrderIndex 1 \
    --Rules.0.EdgeId all \
    --Rules.0.FwGroupId ccn-c0qmm031 \
    --Rules.0.Port -1/-1 \
    --Rules.0.Description one \
    --Rules.0.ParamTemplateId  \
    --Rules.0.BelongMemberId 1300448058 \
    --Rules.1.SourceContent 0.0.0.0/0 \
    --Rules.1.SourceType net \
    --Rules.1.DestContent 0.0.0.0/0 \
    --Rules.1.DestType net \
    --Rules.1.Protocol ANY \
    --Rules.1.RuleAction accept \
    --Rules.1.OrderIndex 2 \
    --Rules.1.EdgeId all \
    --Rules.1.FwGroupId cfwg-e37fa79c \
    --Rules.1.Port -1/-1 \
    --Rules.1.Description 2222 \
    --Rules.1.ParamTemplateId  \
    --Rules.1.BelongMemberId 1300448058
```

Output: 
```
{
    "Response": {
        "GroupId": "fwmrg_0i4eie7e50",
        "RequestId": "0573ab58-ad2c-4bf4-9868-43ba0e066db0"
    }
}
```

