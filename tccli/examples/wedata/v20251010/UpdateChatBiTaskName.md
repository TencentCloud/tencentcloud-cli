**Example 1: 更新对话任务名称**



Input: 

```
tccli wedata UpdateChatBiTaskName --cli-unfold-argument  \
    --Key f2e373ae1770124538118f8664664 \
    --TaskName 查询消费数据1 \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "5646",
            "Key": "f2e373ae1770124538118f8664664",
            "OwnerUin": "700002164619",
            "AppId": "260073493",
            "Owner": "700002164619",
            "WorkspaceId": "17678671667189298",
            "CreatedBy": "700002164619",
            "CreatedOn": "1770124538117",
            "ModifiedBy": "700002164619",
            "ModifiedOn": "1770124913862",
            "RoomKey": "803627528827023360",
            "TaskName": "查询消费数据1",
            "Source": "CHAT_BI",
            "Visibility": "PRIVATE",
            "TaskExtension": "{\"langDataSessionId\":\"22c1e485-5edb-45be-ae88-ed48f54b768c\"}"
        },
        "RequestId": "a5fc4527-f790-46e8-938f-6306fd48aef9"
    }
}
```

