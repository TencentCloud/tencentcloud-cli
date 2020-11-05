**Example 1: Creating a permission group rule**



Input: 

```
tccli cfs CreateCfsRule --cli-unfold-argument  \
    --PGroupId pgroup-12345\
    --RWPermission rw\
    --UserPermission root_squash\
    --AuthClientIp 10.1.1.10\
    --Priority 9
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "RuleId": "rule-12345",
        "PGroupId": "pgroup-12345",
        "AuthClientIp": "10.1.1.10",
        "RWPermission": "rw",
        "UserPermission": "root_squash",
        "Priority": 9
    }
}
```

