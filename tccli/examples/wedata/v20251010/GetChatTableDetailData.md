**Example 1: 明细数据查询**

明细数据查询

Input: 

```
tccli wedata GetChatTableDetailData --cli-unfold-argument  \
    --WorkspaceId 32wer \
    --RoomKey wer \
    --TableKey wer \
    --AsyncTaskId we \
    --Timeout 11
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": {
                "FileUrl": ""
            },
            "Duration": "0",
            "ErrorMessage": "",
            "TaskId": "",
            "TaskStatus": ""
        },
        "RequestId": "38fd7a95-b158-487f-962e-24ebc24202a9"
    }
}
```

