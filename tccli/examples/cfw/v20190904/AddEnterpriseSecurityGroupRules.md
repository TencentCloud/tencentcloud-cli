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
                "SourceContent": "192.168.0.1",
                "DestContent": "192.168.0.2",
                "Protocol": "TCP",
                "Description": "规则详情",
                "RuleUuid": 1,
                "Sequence": 1
            }
        ],
        "RequestId": "d4b7cab1-5594-41fb-88c6-67822af94807"
    }
}
```

