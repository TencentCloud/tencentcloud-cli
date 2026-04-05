**Example 1: 查询列名列表**

查询列名列表

Input: 

```
tccli wedata ListChatTableColumnNames --cli-unfold-argument  \
    --WorkspaceId sdfa \
    --RoomKey sdfsd \
    --TableKeyList sdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "TableColumnInfoList": [
                {
                    "CatalogName": "",
                    "Columns": [],
                    "Key": "",
                    "SchemaName": "",
                    "TableName": "",
                    "TableType": ""
                }
            ]
        },
        "RequestId": "5527593a-0421-4af3-b0bf-f4deb34c45ac"
    }
}
```

