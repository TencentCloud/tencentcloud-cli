**Example 1: 更新文件元信息与内容示例**



Input: 

```
tccli databuddy UpdateFile --cli-unfold-argument  \
    --WorkspaceId 17676920188276733 \
    --FileId 872597305364471808 \
    --FileType NOTEBOOK_FILE \
    --BundleId create_test \
    --BundleInfo {'key1': 'value1'} \
    --Storage.StorageType 1 \
    --Storage.Content ewogICJjZWxscyI6IFsKICAgIHsKICAgICAgImNlbGxfdHlwZSI6ICJjb2RlIiwKICAgICAgImV4ZWN1dGlvbl9jb3VudCI6IG51bGwsCiAgICAgICJtZXRhZGF0YSI6IHt9LAogICAgICAib3V0cHV0cyI6IFtdLAogICAgICAic291cmNlIjogWwogICAgICAgICJwcmludCgxKSIKICAgICAgXSwKICAgICAgImlkIjogImNlbGwtMC0xNzg1ODUxNDg2MTM4IgogICAgfQogIF0sCiAgIm1ldGFkYXRhIjoge30sCiAgIm5iZm9ybWF0IjogNCwKICAibmJmb3JtYXRfbWlub3IiOiA1Cn0=
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "BundleId": "create_test",
            "BundleInfo": "{'key1': 'value1'}",
            "CreateTime": "1785851410",
            "CreateUserUin": "700002164618",
            "FileConfig": {
                "AdvanceConfig": "",
                "DefaultCatalog": "",
                "DefaultSchema": "",
                "ExtraParams": "",
                "OutputConf": [],
                "Params": "eyJtbGZsb3dfcHJlX2V4ZWN1dGVfY29zX3BhdGgiOiJodHRwczovL2J1Y2tldC0zMC0yNTE0MzYxOTEuY29zLmFwLWd1YW5nemhvdS5teXFjbG91ZC5jb20vc2NpLzE3Njc2OTIwMTg4Mjc2NzMzL3BlcnNvbmFsLzcwMDAwMjE2NDYxOC84NzI1OTczMDUzNjQ0NzE4MDgvbm90ZWJvb2tfcHJlbG9hZF9zY3JpcHQucHkifQ==",
                "ResourceId": ""
            },
            "FileId": "872597305364471808",
            "FileName": "create_by_api3.ipynb",
            "FileType": "NOTEBOOK_FILE",
            "OwnerUserName": "wedata30-dev@tencent.com",
            "Path": "/Workspace/Users/create_by_api3.ipynb",
            "Permissions": "[MANAGE]",
            "ReleaseStatus": false,
            "ResourceMode": 0,
            "Status": "active",
            "Storage": {
                "Content": "",
                "StoragePath": "",
                "StorageType": 0
            },
            "UpdateTime": "1785851538",
            "UpdateUserUin": "700002164618",
            "WorkspaceId": "17676920188276733"
        },
        "RequestId": "e5e3c887-81f6-45d4-982e-6d43364fe366"
    }
}
```

