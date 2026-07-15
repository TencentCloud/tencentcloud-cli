**Example 1: 修改VPC 规则**



Input: 

```
tccli fwm ModifyVpcAclRule --cli-unfold-argument  \
    --GroupId fwmrg_aussbmarr2 \
    --Rule.SourceContent 10.10.0.0/16 \
    --Rule.SourceType net \
    --Rule.DestContent 0.0.0.0/0 \
    --Rule.DestType net \
    --Rule.Protocol ANY \
    --Rule.RuleAction drop \
    --Rule.OrderIndex 2 \
    --Rule.EdgeId all \
    --Rule.FwGroupId ccn-c0qmm031 \
    --Rule.RuleId 1293a7fa-b6ee-4243-9429-8e690ce92057 \
    --Rule.Port -1/-1 \
    --Rule.Description two \
    --Rule.ParamTemplateId  \
    --Rule.BelongMemberId 1300448058
```

Output: 
```
{
    "Response": {
        "RequestId": "0c3001bf-d642-4dae-8062-b5cd606238fd"
    }
}
```

