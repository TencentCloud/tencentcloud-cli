**Example 1: 示例**



Input: 

```
tccli databuddy GetFolder --cli-unfold-argument  \
    --WorkspaceId 17799542221324491 \
    --Folder.FolderId 847862709978656768
```

Output: 
```
{
    "Response": {
        "Data": {
            "Folder": {
                "Creator": {
                    "Nickname": "",
                    "UserName": "",
                    "UserTag": "",
                    "UserUin": "700002164618"
                },
                "DeleteTime": "",
                "GitConfig": null,
                "Node": {
                    "AllowActions": [
                        "MANAGE"
                    ],
                    "CreateTime": "1779954223000",
                    "FileId": "847862709978656768",
                    "FileName": "wedata30-dev@tencent.com@700002164618",
                    "FileType": "FOLDER",
                    "IsFavorite": false,
                    "IsSystemGenerated": true,
                    "PathName": "/Workspace/Users/wedata30-dev@tencent.com@700002164618",
                    "UpdateTime": "1779954223000"
                },
                "NodeType": "",
                "OriginPath": "",
                "Owner": {
                    "Nickname": "",
                    "UserName": "",
                    "UserTag": "",
                    "UserUin": "700002164618"
                },
                "Parent": {
                    "AllowActions": [],
                    "CreateTime": "",
                    "FileId": "847862709680861184",
                    "FileName": "",
                    "FileType": "",
                    "IsFavorite": false,
                    "IsSystemGenerated": false,
                    "PathName": "",
                    "UpdateTime": ""
                }
            }
        },
        "RequestId": "4a6bf4b4-449b-493e-8e8a-8b39c6a5c889"
    }
}
```

