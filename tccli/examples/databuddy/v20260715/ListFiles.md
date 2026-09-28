**Example 1: ListFiles**

获取文件夹和文件列表

Input: 

```
tccli databuddy ListFiles --cli-unfold-argument  \
    --WorkspaceId 17697****0**47629 \
    --Parent.FolderId 86553********46400 \
    --NameKeyword 071*****
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Creator": {
                        "Nickname": "we***a*************t.com",
                        "UserName": "weda**3**********ent.com",
                        "UserTag": "0",
                        "UserUin": "70*******618"
                    },
                    "DeleteTime": "",
                    "GitConfig": null,
                    "Node": {
                        "AllowActions": [
                            "MANAGE"
                        ],
                        "CreateTime": "1784168588000",
                        "FileId": "865539****5***5136",
                        "FileName": "07161023.ipynb",
                        "FileType": "NOTEBOOK_FILE",
                        "IsFavorite": false,
                        "IsSystemGenerated": false,
                        "PathName": "/Workspace/Users/weda********@tenc***************64618/0716/07161023.ipynb",
                        "UpdateTime": "1784168790000"
                    },
                    "NodeType": "",
                    "OriginPath": "",
                    "Owner": {
                        "Nickname": "",
                        "UserName": "",
                        "UserTag": "",
                        "UserUin": "700*******18"
                    },
                    "Parent": {
                        "AllowActions": [],
                        "CreateTime": "",
                        "FileId": "86553*********6400",
                        "FileName": "",
                        "FileType": "",
                        "IsFavorite": false,
                        "IsSystemGenerated": false,
                        "PathName": "",
                        "UpdateTime": ""
                    }
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "6decf098-7409-4899-8018-a563aa53fa73"
    }
}
```

