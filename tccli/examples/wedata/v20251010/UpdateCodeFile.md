**Example 1: 更新代码文件**



Input: 

```
tccli wedata UpdateCodeFile --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --CodeFileId 804392248570023936 \
    --ExtensionType NOTEBOOK_FILE \
    --CodeFileConfig.Params 1 \
    --CodeFileConfig.ResourceId 1 \
    --CodeFileConfig.DefaultCatalog 1 \
    --CodeFileConfig.DefaultSchema 1 \
    --CodeFileConfig.AdvanceConfig 1 \
    --CodeFileConfig.ExtraParams 1 \
    --BundleId 1 \
    --BundleInfo 1
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
                "Content": "",
                "StoragePath": "",
                "StorageType": 0
            },
            "UpdateTime": "1769590057",
            "UpdateUserUin": "700002164618",
            "WorkspaceId": "17663856806379896"
        },
        "RequestId": "e404f27f-eec7-4c46-a029-3588fe336958"
    }
}
```

