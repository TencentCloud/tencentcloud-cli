**Example 1: openapi回收权限**

openapi回收权限

Input: 

```
tccli wedata RevokePrivileges --cli-unfold-argument  \
    --Resources.0.ResourceType CATALOG \
    --Resources.0.ResourceUri tclake_lakehouse_catalog_table_mayxxiao_64longlonglonglonglonglo \
    --Subjects.0.SubjectType User \
    --Subjects.0.SubjectValues 700002130525 \
    --Privileges.0.Name SELECT_TABLE
```

Output: 
```
{
    "Response": {
        "Data": {
            "OverallSuccess": true,
            "Results": [
                {
                    "Reason": "",
                    "Resource": {
                        "ResourceType": "CATALOG",
                        "ResourceUri": "tclake_lakehouse_catalog_table_mayxxiao_64longlonglonglonglonglo"
                    },
                    "Result": true
                }
            ]
        },
        "RequestId": "17b4ff0e-bc89-4169-b9cb-8581565a9dfe"
    }
}
```

