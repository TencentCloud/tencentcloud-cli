**Example 1: 停止学习字段**

停止学习字段

Input: 

```
tccli wedata StopChatTableColumnLearning --cli-unfold-argument  \
    --WorkspaceId 17635174232904110 \
    --RoomKey asdfa \
    --TableKey sadfa \
    --ColumnKeys asdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnKey": ""
        },
        "RequestId": "ce82e00a-8bc6-4935-beed-6abc180ad927"
    }
}
```

