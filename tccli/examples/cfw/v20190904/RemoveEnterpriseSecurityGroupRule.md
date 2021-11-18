**Example 1: 删除新企业安全组规则**



Input: 

```
tccli cfw RemoveEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RemoveType 0 \
    --RuleUuid 8888
```

Output: 
```
{
    "Response": {
        "RuleUuid": 8888,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Status": 0
    }
}
```

