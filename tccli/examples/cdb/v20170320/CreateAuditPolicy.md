**Example 1: 创建审计策略**



Input: 

```
tccli cdb CreateAuditPolicy --cli-unfold-argument  \
    --Name audit_policy_1 \
    --RuleId cdbrule-asdfghjk \
    --InstanceId cdb-qwerasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "PolicyId": "cdbpolicy-asdfqwer"
    }
}
```

