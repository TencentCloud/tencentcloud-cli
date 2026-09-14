**Example 1: 获取文件信息示例**

查询文件元信息与内容

Input: 

```
tccli databuddy GetFile --cli-unfold-argument  \
    --WorkspaceId 17676920188276733 \
    --FileId 837014075591299072 \
    --FileType NOTEBOOK_FILE \
    --IncludeContent False \
    --VersionId 872595707510808576 \
    --FilePath /Workspace/Users/xingyundong@700002355291/abc.ipynb
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "BundleId": "",
            "BundleInfo": "",
            "CreateTime": "1777367707",
            "CreateUserUin": "700002164618",
            "FileConfig": {
                "AdvanceConfig": "",
                "DefaultCatalog": "",
                "DefaultSchema": "",
                "ExtraParams": "",
                "OutputConf": [],
                "Params": "eyJtbGZsb3dfcHJlX2V4ZWN1dGVfY29zX3BhdGgiOiIifQ==",
                "ResourceId": ""
            },
            "FileId": "837014075591299072",
            "FileName": "abc.ipynb",
            "FileType": "NOTEBOOK_FILE",
            "OwnerUserName": "wedata30-dev@tencent.com",
            "Path": "/Workspace/Users/xingyundong@700002355291/abc.ipynb",
            "Permissions": "[MANAGE]",
            "ReleaseStatus": false,
            "ResourceMode": 1,
            "Status": "active",
            "Storage": {
                "Content": "",
                "StoragePath": "",
                "StorageType": 0
            },
            "UpdateTime": "1785851029",
            "UpdateUserUin": "700002164618",
            "WorkspaceId": "17676920188276733"
        },
        "RequestId": "30507de5-777a-48b0-ab08-c86597439dd5"
    }
}
```

