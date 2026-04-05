**Example 1: 关联详情**

关联详情

Input: 

```
tccli wedata GetChatTableRelation --cli-unfold-argument  \
    --WorkspaceId 1 \
    --RoomKey 1 \
    --RelationKey 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "",
            "CreatedBy": "",
            "CreatedOn": "0",
            "Id": "0",
            "Key": "",
            "LeftColumn": {
                "ColumnKey": "",
                "ColumnName": "",
                "ErrorInfo": "column not found:null"
            },
            "LeftTable": {
                "CatalogName": "",
                "ErrorInfo": "table not found:null",
                "Name": "",
                "SchemaName": "",
                "TableKey": ""
            },
            "ModifiedBy": "",
            "ModifiedOn": "0",
            "Owner": "",
            "OwnerUin": "",
            "RelationType": "",
            "RightColumn": {
                "ColumnKey": "",
                "ColumnName": "",
                "ErrorInfo": "column not found:null"
            },
            "RightTable": {
                "CatalogName": "",
                "ErrorInfo": "table not found:null",
                "Name": "",
                "SchemaName": "",
                "TableKey": ""
            },
            "WorkspaceId": ""
        },
        "RequestId": "10ad31a1-d316-4ee5-a14a-a05f994cc71c"
    }
}
```

