**Example 1: 成功响应**



Input: 

```
tccli wedata GetCodeFileVersion --cli-unfold-argument  \
    --CodeFileId 74a0cab9-ed79-4432-8c79-e8e6ed623861 \
    --WorkspaceId workspaceId_test \
    --VersionValue 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "CodeFileId": "74a0cab9-ed79-4432-8c79-e8e6ed623861",
            "CreateTime": "1761939687929",
            "CreateUserUin": "700002164618",
            "Description": "",
            "OwnerUin": "700002164618",
            "UpdateTime": "1761939687929",
            "UpdateUserUin": "700002164618",
            "VersionId": "v1",
            "VersionValue": 0,
            "WorkspaceId": "workspaceId_test"
        },
        "RequestId": "1a3db898-27ea-4ba5-bc0e-1a9ccfe2c053"
    }
}
```

