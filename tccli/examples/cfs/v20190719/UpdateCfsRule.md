**Example 1: Updating a permission group rule**



Input: 

```
tccli cfs UpdateCfsRule --cli-unfold-argument  \
    --RuleId rule-12345\
    --PGroupId pgroup-12345\
    --AuthClientIp 10.0.0.10\
    --RWPermission rw\
    --UserPermission no_root_squash\
    --Priority 7
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "PGroupId": "pgroup-12345",
        "RuleId": "rule-12345",
        "AuthClientIp": "10.0.0.10",
        "RWPermission": "rw",
        "UserPermission": "no_root_squash",
        "Priority": 7
    }
}
```

