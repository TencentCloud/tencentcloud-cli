**Example 1: 更新权限组规则**



Input: 

```
tccli cfs UpdateCfsRule --cli-unfold-argument  \
    --RWPermission rw \
    --Priority 7 \
    --PGroupId pgroup-12345 \
    --RuleId rule-12345 \
    --AuthClientIp 10.0.0.10 \
    --UserPermission no_root_squash
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

