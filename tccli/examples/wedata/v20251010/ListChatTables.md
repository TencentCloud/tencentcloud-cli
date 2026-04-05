**Example 1: 查看数据表列表**

查看数据表列表

Input: 

```
tccli wedata ListChatTables --cli-unfold-argument  \
    --WorkspaceId sdfad \
    --RoomKey asdfads \
    --PageRequest.AllPage True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppId": "",
                    "CatalogName": "",
                    "CreatedBy": "",
                    "CreatedOn": "0",
                    "ErrorCode": "",
                    "ErrorInfo": "",
                    "Id": "0",
                    "Key": "",
                    "LearningStatus": "",
                    "ModifiedBy": "",
                    "ModifiedOn": "0",
                    "Owner": "",
                    "OwnerUin": "",
                    "SchemaName": "",
                    "TableName": "",
                    "TableType": "",
                    "WorkspaceId": ""
                }
            ]
        },
        "RequestId": "58e03391-57cd-4332-b18d-5545dfe8dd2b"
    }
}
```

