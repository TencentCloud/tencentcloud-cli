**Example 1: demo**



Input: 

```
tccli wedata GetFolderNodePath --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --Meta.FileId 791609522331598848
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
        "RequestId": "600c3b1b-752a-446d-b9c0-adaa71e47290"
    }
}
```

