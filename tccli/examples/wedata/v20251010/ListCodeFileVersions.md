**Example 1: 查询文件版本列表**

查询文件版本列表

Input: 

```
tccli wedata ListCodeFileVersions --cli-unfold-argument  \
    --CodeFileId 793146230887493632 \
    --WorkspaceId 17622177773248536 \
    --PageNumber 1 \
    --PageSize 1 \
    --ReleaseStatus True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppId": "251436191",
                    "CodeFileConfig": "{\"Params\":\"2\",\"ResourceId\":\"22\",\"DefaultCatalog\":\"12\",\"DefaultSchema\":\"22\",\"AdvanceConfig\":\"22\",\"ExtraParams\":\"22\"}",
                    "CodeFileId": "793146230887493632",
                    "CreateTime": "1766930573310",
                    "CreateUserName": "wedata30-dev@tencent.com",
                    "CreateUserUin": "700002164618",
                    "Description": "",
                    "OwnerUin": "700002164618",
                    "ReleaseStatus": true,
                    "UpdateTime": "1766930573310",
                    "UpdateUserName": "wedata30-dev@tencent.com",
                    "UpdateUserUin": "700002164618",
                    "VersionId": "793237566495993856",
                    "VersionValue": 2,
                    "WorkspaceId": "17622177773248536"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": "2",
            "TotalPageNumber": "2"
        },
        "RequestId": "1bff9e9e-0d47-417a-be02-a387927c3dee"
    }
}
```

