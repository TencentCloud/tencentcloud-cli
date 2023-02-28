**Example 1: 编辑新企业安全组规则**

编辑新企业安全组规则

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 1 \
    --Data.OrderIndex xx \
    --Data.Protocol xx \
    --Data.SourceType xx \
    --Data.SourceContent xx \
    --Data.DestType xx \
    --Data.ServiceTemplateId xx \
    --Data.DestContent xx \
    --Data.RuleAction xx \
    --Data.Port xx \
    --Data.Description xx \
    --ModifyType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Status": 0,
        "NewRuleUuid": 35641
    }
}
```

