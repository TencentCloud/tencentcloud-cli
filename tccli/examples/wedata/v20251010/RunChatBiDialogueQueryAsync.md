**Example 1: 异步执行对话查询**



Input: 

```
tccli wedata RunChatBiDialogueQueryAsync --cli-unfold-argument  \
    --Key c881a57b1770110715224800d0733 \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360 \
    --Sql U0VMRUNUICBtaS5tb3ZpZV9uYW1lIEFTIG1vdmllX25hbWUsCiAgICAgICAgbWkucmF0aW5nIEFTIHJhdGluZywKICAgICAgICBtaS5idWRnZXQgQVMgYnVkZ2V0LAogICAgICAgIFNVTShkYm8ucmV2ZW51ZSkgQVMgdG90YWxfcmV2ZW51ZQpGUk9NICAgIGBEYXRhTGFrZUNhdGFsb2dgLmBjaGF0YmlgLmBkYWlseV9ib3hfb2ZmaWNlYCBBUyBkYm8KTEVGVCBKT0lOIGBEYXRhTGFrZUNhdGFsb2dgLmBjaGF0YmlgLmBtb3ZpZV9pbmZvYCBBUyBtaQpPTiAgICAgIGRiby5tb3ZpZV9pZCA9IG1pLm1vdmllX2lkCkdST1VQIEJZIG1pLm1vdmllX25hbWUsCiAgICAgICAgIG1pLnJhdGluZywKICAgICAgICAgbWkuYnVkZ2V0Ck9SREVSIEJZIHRvdGFsX3JldmVudWUgREVTQwpMSU1JVCAgIDEwOw== \
    --SqlModified False
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "task_29d3c0555227495298edd66d1d5f50b1",
            "TaskStatus": "PENDING",
            "Data": "",
            "ErrorMessage": "",
            "Duration": "0"
        },
        "RequestId": "7e864d39-903b-4c30-a3fe-33e553c95b7c"
    }
}
```

