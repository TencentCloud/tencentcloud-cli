**Example 1: 查询审计策略**



Input: 

```
tccli cdb DescribeAuditPolicies --cli-unfold-argument  \
    --InstanceId cdb-qwerasdf \
    --PolicyId cdbpolicy-asdfqwer
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "PolicyId": "cdbpolicy-asdfqwer",
                "Status": "running",
                "InstanceId": "cdb-qwerasdf",
                "InstanceName": "test",
                "CreateTime": "2019-03-20 17:09:13",
                "ModifyTime": "2019-03-20 17:09:13",
                "PolicyName": "audit_policy_1",
                "RuleId": "cdbrule-asdfqwer",
                "RuleName": "audit1"
            }
        ]
    }
}
```

