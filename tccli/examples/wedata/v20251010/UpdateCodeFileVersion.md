**Example 1: 成功响应**



Input: 

```
tccli wedata UpdateCodeFileVersion --cli-unfold-argument  \
    --CodeFileId 74a0cab9-ed79-4432-8c79-e8e6ed623861 \
    --WorkspaceId workspaceId_test \
    --VersionValue 1 \
    --Description 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "1300055887",
            "CodeFileId": "74a0cab9-ed79-4432-8c79-e8e6ed623861",
            "CreateTime": "1761939687929",
            "CreateUserName": "",
            "CreateUserUin": "700002164618",
            "Description": "12",
            "OwnerUin": "700002164618",
            "UpdateTime": "1763373378679",
            "UpdateUserName": "",
            "UpdateUserUin": "600000561778",
            "VersionId": "v1",
            "VersionValue": 1,
            "WorkspaceId": "workspaceId_test"
        },
        "RequestId": "aa81f78e-eae9-43c6-9766-a9898e1f3465"
    }
}
```

