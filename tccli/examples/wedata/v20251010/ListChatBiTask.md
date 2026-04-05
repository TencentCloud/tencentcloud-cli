**Example 1: 查询对话任务列表**



Input: 

```
tccli wedata ListChatBiTask --cli-unfold-argument  \
    --UserId 700002164619 \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360 \
    --Source CHAT_BI \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 100 \
    --PageRequest.AllPage False
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 100,
                "TotalCount": 69,
                "TotalPageNumber": 1
            },
            "Items": [
                {
                    "Id": "5646",
                    "Key": "f2e373ae1770124538118f8664664",
                    "OwnerUin": "700002164619",
                    "AppId": "260073493",
                    "Owner": "wedata30-test1@tencent.com",
                    "WorkspaceId": "17678671667189298",
                    "CreatedBy": "wedata30-test1@tencent.com",
                    "CreatedOn": "1770124538117",
                    "ModifiedBy": "wedata30-test1@tencent.com",
                    "ModifiedOn": "1770124538205",
                    "RoomKey": "803627528827023360",
                    "TaskName": "查询消费数据",
                    "Source": "CHAT_BI",
                    "Visibility": "PRIVATE",
                    "TaskExtension": "{\"langDataSessionId\":\"22c1e485-5edb-45be-ae88-ed48f54b768c\"}"
                }
            ]
        },
        "RequestId": "59337172-a87f-4d6d-be12-66d985cebd28"
    }
}
```

