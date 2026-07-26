**Example 1: 按规则 ID 精确删除企业安全组规则**

删除 RuleUuid 指定的企业安全组规则。

Input: 

```
tccli cfw RemoveEnterpriseSecurityGroupRule --cli-unfold-argument  \
    --RemoveType 0 \
    --RuleUuid 42001
```

Output: 
```
{
    "Response": {
        "RuleUuid": 42001,
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "Status": 0
    }
}
```

