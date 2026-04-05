**Example 1: 查询数据表详情**

查询数据表详情

Input: 

```
tccli wedata GetChatTable --cli-unfold-argument  \
    --WorkspaceId sdfads \
    --RoomKey sdafd \
    --TableKey sdfa
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "",
            "CatalogName": "",
            "Columns": [
                {
                    "AppId": "",
                    "Comment": "",
                    "CreatedBy": "",
                    "CreatedOn": "0",
                    "EnableExample": 0,
                    "EnableValueDict": 0,
                    "ExampleLearningErrorInfo": "",
                    "ExampleLearningStatus": "",
                    "ExampleList": [],
                    "Id": "0",
                    "Key": "",
                    "ModifiedBy": "",
                    "ModifiedOn": "0",
                    "Name": "",
                    "NeedUpdate": false,
                    "Owner": "",
                    "OwnerUin": "",
                    "SynonymList": [],
                    "Type": "",
                    "UserComment": "",
                    "ValueDictLearningErrorInfo": "",
                    "ValueDictLearningStatus": "",
                    "ValueDistinctCount": "",
                    "VisibleStatus": 0,
                    "WorkspaceId": ""
                }
            ],
            "Comment": "",
            "CreatedBy": "",
            "CreatedOn": "0",
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
            "UserComment": "",
            "WorkspaceId": ""
        },
        "RequestId": "ffa56654-d69a-47bc-96a2-403a8566690a"
    }
}
```

