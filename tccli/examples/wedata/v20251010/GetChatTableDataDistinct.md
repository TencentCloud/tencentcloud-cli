**Example 1: 唯一值查询**

唯一值查询

Input: 

```
tccli wedata GetChatTableDataDistinct --cli-unfold-argument  \
    --WorkspaceId sdafa \
    --RoomKey sdfsdfsd \
    --TableKey asdaf \
    --ColumnKeyList sdf \
    --Limit 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": {
                "ColumnDistinctDataList": []
            },
            "Duration": "0",
            "ErrorMessage": "",
            "TaskId": "",
            "TaskStatus": ""
        },
        "RequestId": "3c870dba-b56c-424a-be9e-22babc286598"
    }
}
```

