**Example 1: demo**



Input: 

```
tccli wedata ListFiles --cli-unfold-argument  \
    --WorkspaceId 17622177773248536
```

Output: 
```
{
    "Response": {
        "Data": {
            "Nodes": [
                {
                    "Creator": {
                        "Nickname": "",
                        "Uin": "",
                        "UserName": "",
                        "UserTag": ""
                    },
                    "DeleteTime": "",
                    "Node": {
                        "AllowActions": [
                            "MANAGE"
                        ],
                        "Attribute": {
                            "IsSystemGenerated": true,
                            "PathName": "/GitFolder",
                            "VersionId": ""
                        },
                        "CreateTime": "1766542418",
                        "FileId": "L0dpdEZvbGRlcg==",
                        "FileName": "GitFolder",
                        "FileType": "GIT_FOLDER",
                        "IsFavorite": false,
                        "ModifyTime": "1769148951",
                        "Storage": {
                            "Content": "",
                            "StoragePath": "",
                            "StorageType": 0
                        }
                    },
                    "NodeType": "",
                    "OriginPath": "",
                    "Owner": {
                        "Nickname": "",
                        "Uin": "",
                        "UserName": "",
                        "UserTag": ""
                    },
                    "Parent": {
                        "AllowActions": [],
                        "Attribute": {
                            "IsSystemGenerated": false,
                            "PathName": "",
                            "VersionId": ""
                        },
                        "CreateTime": "",
                        "FileId": "",
                        "FileName": "",
                        "FileType": "",
                        "IsFavorite": false,
                        "ModifyTime": "",
                        "Storage": {
                            "Content": "",
                            "StoragePath": "",
                            "StorageType": 0
                        }
                    }
                }
            ],
            "PageResponse": {
                "ExtendInfo": "",
                "PageNumber": 1,
                "PageSize": 0,
                "TotalCount": 2,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "6091652b-db79-460f-986d-3b672c37ac2a"
    }
}
```

