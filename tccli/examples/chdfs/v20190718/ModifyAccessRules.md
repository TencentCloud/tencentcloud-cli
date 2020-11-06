**Example 1: 批量修改权限规则属性**

批量修改权限规则属性

Input: 

```
tccli chdfs ModifyAccessRules --cli-unfold-argument  \
    --AccessRules.0.AccessRuleId 13001 \
    --AccessRules.0.Address 127.0.0.1 \
    --AccessRules.0.AccessMode 1 \
    --AccessRules.0.Priority 2 \
    --AccessRules.1.AccessRuleId 13002 \
    --AccessRules.1.Address 127.0.0.1 \
    --AccessRules.1.AccessMode 1 \
    --AccessRules.1.Priority 1
```

Output: 
```
{
    "Response": {
        "RequestId": "baaf73f9-0c42-441b-afdb-b9da71a50f47"
    }
}
```

