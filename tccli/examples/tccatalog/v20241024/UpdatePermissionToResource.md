**Example 1: 更新指定资源下用户权限**



Input: 

```
tccli tccatalog UpdatePermissionToResource --cli-unfold-argument  \
    --FullName DataLakeCatalog.create_test3.test_create_table \
    --Type table \
    --RolePrivileges.0.GrantPrivileges.0.Name DROP_TABLE \
    --RolePrivileges.0.GrantPrivileges.0.Condition ALLOW \
    --RolePrivileges.0.UserId 700002195767 \
    --RolePrivileges.0.ObjectType UserId
```

Output: 
```
{
    "Response": {
        "RequestId": "83eac956-3c09-4c18-8745-fc3096512796"
    }
}
```

