**Example 1: 列出权限**

列出权限

Input: 

```
tccli tccatalog DescribeRolePermissionList --cli-unfold-argument  \
    --RoleId 4
```

Output: 
```
{
    "Response": {
        "RequestId": "cef1a07d-9d8e-4a79-bc01-bde002cb5fb2",
        "SecurableObjects": [
            {
                "FullName": "catalogA",
                "Privileges": [
                    {
                        "Condition": "allow",
                        "Name": "use_schema"
                    },
                    {
                        "Condition": "allow",
                        "Name": "use_catalog"
                    }
                ],
                "Type": "catalog"
            }
        ]
    }
}
```

