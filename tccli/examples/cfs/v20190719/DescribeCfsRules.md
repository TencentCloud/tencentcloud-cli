**Example 1: 查询权限组规则**



Input: 

```
tccli cfs DescribeCfsRules --cli-unfold-argument  \
    --PGroupId pgroup-12345
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

