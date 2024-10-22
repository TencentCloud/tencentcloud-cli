**Example 1: 编辑新企业安全组规则**

编辑新企业安全组规则

Input: 

```
tccli cfw ModifyEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RuleUuid 1 \
    --Data.OrderIndex 1 \
    --Data.Protocol TCP \
    --Data.SourceType net \
    --Data.SourceContent 192.168.0.2 \
    --Data.DestType net \
    --Data.ServiceTemplateId  \
    --Data.DestContent 192.168.0.3 \
    --Data.RuleAction accept \
    --Data.Port 80 \
    --Data.Description 放行规则 \
    --ModifyType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8f563b4d-8151-4db0-a822-9bde279d2079",
        "Status": 0,
        "NewRuleUuid": 3
    }
}
```

