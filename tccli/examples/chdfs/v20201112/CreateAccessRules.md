**Example 1: 批量创建权限规则**

批量创建权限规则

Input: 

```
tccli chdfs CreateAccessRules --cli-unfold-argument  \
    --AccessRules.0.Priority 2 \
    --AccessRules.0.AccessMode 2 \
    --AccessRules.0.Address 127.0.0.1 \
    --AccessRules.1.Priority 1 \
    --AccessRules.1.AccessMode 1 \
    --AccessRules.1.Address 127.0.0.1 \
    --AccessGroupId ag-jwmfdcul
```

Output: 
```
{
    "Response": {
        "AccessRules": [
            {
                "AccessRuleId": 13001,
                "Address": "127.0.0.1",
                "AccessMode": 1,
                "Priority": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            },
            {
                "AccessRuleId": 13002,
                "Address": "127.0.0.1",
                "AccessMode": 2,
                "Priority": 2,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            }
        ],
        "RequestId": "5d6d3ef8-db1d-40de-afa1-d340302458bb"
    }
}
```

