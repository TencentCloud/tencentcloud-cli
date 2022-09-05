**Example 1: 创建权限组规则**



Input: 

```
tccli cfs CreateCfsRule --cli-unfold-argument  \
    --RWPermission rw \
    --AuthClientIp 10.1.1.10 \
    --PGroupId pgroup-12345 \
    --Priority 9 \
    --UserPermission root_squash
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

