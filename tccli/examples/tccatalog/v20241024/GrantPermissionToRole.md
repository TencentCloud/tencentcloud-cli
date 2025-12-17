**Example 1: 添加权限**

添加权限

Input: 

```
tccli tccatalog GrantPermissionToRole --cli-unfold-argument  \
    --RoleId 3 \
    --SecurableObjects.0.FullName catalog1 \
    --SecurableObjects.0.Type catalog \
    --SecurableObjects.0.Privileges.0.Name use_catalog \
    --SecurableObjects.0.Privileges.0.Condition allow
```

Output: 
```
{
    "Response": {
        "RequestId": "a246ba0a-8947-45c1-88de-31c83061a4bd"
    }
}
```

