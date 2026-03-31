**Example 1: 查询代码文件**

查询代码文件

Input: 

```
tccli wedata GetCodeFile --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --ExtensionType NOTEBOOK_FILE \
    --CodeFileId 804392248570023936 \
    --IncludeContent True
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "BundleId": "1",
            "BundleInfo": "1",
            "CodeFileConfig": {
                "AdvanceConfig": "1",
                "DefaultCatalog": "1",
                "DefaultSchema": "1",
                "ExtraParams": "1",
                "Params": "1",
                "ResourceId": "1"
            },
            "CodeFileId": "804392248570023936",
            "CodeFileName": "test0128-1.ipynb",
            "CreateTime": "1769590057",
            "CreateUserUin": "700002164618",
            "ExtensionType": "NOTEBOOK_FILE",
            "InchargeUserUin": "700002164618",
            "ParentFolderId": "798557598625202176",
            "Path": "/Workspace/junoren/test0128-1.ipynb",
            "Permissions": "[MANAGE]",
            "ReleaseStatus": false,
            "Status": "active",
            "Storage": {
                "Content": "ewogImNlbGxzIjogWwogIHsKICAgImNlbGxfdHlwZSI6ICJjb2RlIiwKICAgImV4ZWN1dGlvbl9jb3VudCI6IG51bGwsCiAgICJtZXRhZGF0YSI6IHt9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogW10KICB9CiBdLAogIm1ldGFkYXRhIjoge30sCiAibmJmb3JtYXQiOiA0LAogIm5iZm9ybWF0X21pbm9yIjogNQp9",
                "StoragePath": "",
                "StorageType": 1
            },
            "UpdateTime": "1769590057",
            "UpdateUserUin": "700002164618",
            "WorkspaceId": "17663856806379896"
        },
        "RequestId": "17a165cd-7de4-44b8-8c18-06b209b53a2c"
    }
}
```

