**Example 1: 添加VPC 规则**



Input: 

```
tccli fwm CreateVpcAclRule --cli-unfold-argument  \
    --GroupId fwmrg_aussbmarr2 \
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
    --Rules.0.Description zero \
    --Rules.0.ParamTemplateId  \
    --Rules.0.BelongMemberId 1300448058
```

Output: 
```
{
    "Response": {
        "RequestId": "c4b0ec1c-82a7-4781-b73e-86c0623187b6"
    }
}
```

