**Example 1: 批量创建权限规则**

批量创建权限规则

Input: 

```
tccli chdfs CreateAccessRules --cli-unfold-argument  \
    --AccessGroupId ag-jwmfdcul \
    --AccessRules.0.Address 127.0.0.1 \
    --AccessRules.0.AccessMode 1 \
    --AccessRules.0.Priority 1 \
    --AccessRules.1.Address 127.0.0.1 \
    --AccessRules.1.AccessMode 2 \
    --AccessRules.1.Priority 2
```

Output: 
```
{
    "Response": {
        "RequestId": "5d6d3ef8-db1d-40de-afa1-d340302458bb"
    }
}
```

