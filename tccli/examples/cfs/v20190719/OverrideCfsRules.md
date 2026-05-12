**Example 1: 批量创建权限组规则**



Input: 

```
tccli cfs OverrideCfsRules --cli-unfold-argument  \
    --PermissionGroupId pgroup-12345 \
    --RuleList.0.RWPermission rw \
    --RuleList.0.AuthClientIp 10.1.1.10 \
    --RuleList.0.UserPermission root_squash \
    --RuleList.0.Priority 9
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "RuleList": [
            {
                "RuleId": "rule-12345",
                "AuthClientIp": "10.1.1.100",
                "RWPermission": "rw",
                "UserPermission": "root_squash",
                "Priority": 7
            }
        ]
    }
}
```

