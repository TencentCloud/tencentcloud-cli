**Example 1: 查询安全实例列表**



Input: 

```
tccli teo DescribeSecurityPolicyList --cli-unfold-argument  \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "RequestId": "45f43eef-60e0-4be2-b322-327eca853592",
        "SecurityEntities": [
            {
                "Entity": "*.eosecdev.xyz",
                "EntityType": "domain",
                "ZoneId": "zone-285thql0vdhi"
            },
            {
                "Entity": "a.eosecdev.xyz",
                "EntityType": "domain",
                "ZoneId": "zone-285thql0vdhi"
            },
            {
                "Entity": "b.eosecdev.xyz",
                "EntityType": "domain",
                "ZoneId": "zone-285thql0vdhi"
            }
        ]
    }
}
```

