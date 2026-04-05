**Example 1: 获取列详情**

获取列详情

Input: 

```
tccli wedata GetChatTableColumn --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
    --RoomKey 92bdc2500ed64bfe1764916241071a4fc7c5f40d883f9 \
    --TableKey 97d83216dc1949f717664825858548e0fa5040dd5b38d \
    --ColumnKey 976acbe4eb6e420717664825875199ab85d86e372c748
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "9c298d7f-2138-42e1-a227-054e733d3bbe"
    }
}
```

