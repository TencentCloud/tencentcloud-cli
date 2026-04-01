**Example 1: demo**



Input: 

```
tccli wedata GetFiles --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --Metas.0.FileId 791609522159632384
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
                            "PathName": "/Workspace",
                            "VersionId": ""
                        },
                        "CreateTime": "1766542418",
                        "FileId": "791609522159632384",
                        "FileName": "Workspace",
                        "FileType": "FOLDER",
                        "IsFavorite": false,
                        "ModifyTime": "1769148589",
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
            ]
        },
        "RequestId": "e5655705-e3e8-4347-a464-3299f02f9fa1"
    }
}
```

