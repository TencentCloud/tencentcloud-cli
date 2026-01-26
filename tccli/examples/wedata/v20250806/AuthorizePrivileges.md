**Example 1: openapi授权**

openapi授权

Input: 

```
tccli wedata AuthorizePrivileges --cli-unfold-argument  \
    --Resources.0.ResourceType CATALOG \
    --Resources.0.ResourceUri tclake_lakehouse_catalog_table_mayxxiao_64longlonglonglonglonglo \
    --Subjects.0.SubjectType User \
    --Subjects.0.SubjectValues 700002130525 \
    --Privileges.0.Name USE_CATALOG
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
        "RequestId": "66718386-3bca-4664-8c69-2ad088a69fc6"
    }
}
```

