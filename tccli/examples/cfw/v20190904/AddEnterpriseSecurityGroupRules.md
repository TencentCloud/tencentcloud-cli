**Example 1: 创建新企业安全组规则**

创建新企业安全组规则

Input: 

```
tccli cfw AddEnterpriseSecurityGroupRules --cli-unfold-argument  \
    --Data.0.OrderIndex 1 \
    --Data.0.Protocol TCP \
    --Data.0.SourceType net \
    --Data.0.SourceContent 192.168.0.1 \
    --Data.0.DestType net \
    --Data.0.DestContent 192.168.0.2 \
    --Data.0.RuleAction accept \
    --Data.0.Port 80 \
    --Data.0.Description 规则详情
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Rules": [
            {
                "SourceContent": "abc",
                "DestContent": "abc",
                "Protocol": "abc",
                "Description": "abc",
                "RuleUuid": 0,
                "Sequence": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

