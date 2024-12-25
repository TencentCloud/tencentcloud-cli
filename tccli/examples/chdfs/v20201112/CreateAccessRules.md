**Example 1: 批量创建权限规则**

批量创建权限规则

Input: 

```
tccli chdfs CreateAccessRules --cli-unfold-argument  \
    --AccessRules.0.Address 10.0.0.0/24 \
    --AccessRules.0.AccessMode 1 \
    --AccessRules.0.Priority 1 \
    --AccessGroupId ag-gei2xxxx
```

Output: 
```
{
    "Response": {
        "AccessRules": [
            {
                "AccessMode": 1,
                "AccessRuleId": 900,
                "Address": "10.0.0.0/24",
                "CreateTime": "2024-12-25T19:35:20+08:00",
                "Priority": 1
            }
        ],
        "RequestId": "c94d61f1-dd9b-472a-910a-5dc07cedaae7"
    }
}
```

