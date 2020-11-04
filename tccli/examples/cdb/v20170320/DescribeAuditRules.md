**Example 1: 查询审计规则**



Input: 

```
tccli cdb DescribeAuditRules --cli-unfold-argument  \
    --RuleId "cdbrule-qwerasdf"
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "RuleId": "cdbrule-qwerasdf",
                "CreateTime": "2019-03-20 17:09:13",
                "ModifyTime": "2019-03-20 17:09:13",
                "RuleName": "audit1",
                "Description": "audit_test",
                "AuditAll": true
            }
        ]
    }
}
```

