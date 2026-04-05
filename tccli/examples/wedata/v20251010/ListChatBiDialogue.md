**Example 1: 查询对话列表**



Input: 

```
tccli wedata ListChatBiDialogue --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360 \
    --ChatTaskKey 2f0cb0171770123865120dacd3f5b \
    --ChatTypes CHAT_QUERY_DATA \
    --UserId 700002164619 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 20 \
    --PageRequest.AllPage False
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 20,
                "TotalCount": 1,
                "TotalPageNumber": 1
            },
            "Items": [
                {
                    "Id": "6339",
                    "Key": "293cfe981770123865126cc7f65fd",
                    "OwnerUin": "700002164619",
                    "AppId": "260073493",
                    "WorkspaceId": "17678671667189298",
                    "Owner": "wedata30-test1@tencent.com",
                    "CreatedBy": "wedata30-test1@tencent.com",
                    "CreatedOn": "1770123865125",
                    "ModifiedBy": "wedata30-test1@tencent.com",
                    "ModifiedOn": "1770123880565",
                    "RoomKey": "803627528827023360",
                    "ChatTaskKey": "2f0cb0171770123865120dacd3f5b",
                    "DialogueDisplayKey": "dialogue_1770123865125",
                    "Query": "查询电影数量",
                    "QueryContent": "",
                    "ResultContent": "{\"dialogueId\":6339,\"traceId\":\"f7576e96-fad6-4fff-91fd-e923ca931f69\",\"taskKey\":\"2f0cb0171770123865120dacd3f5b\",\"dialogueKey\":\"293cfe981770123865126cc7f65fd\",\"roomKey\":\"803627528827023360\",\"workspaceId\":\"17678671667189298\",\"connectionId\":\"connectionId_0d9fef72_f7576e96-fad6-4fff-91fd-e923ca931f69\",\"chatType\":\"CHAT_QUERY_DATA\",\"code\":1502251,\"costTime\":15414,\"timestamp\":1770123880545,\"errorDetail\":\"ErrorCode:[1502251], ErrorDescription:[SSE message send failed]\",\"data\":{\"questionUnderstandingStepData\":{\"timestamp\":1770123877833,\"extraData\":{\"chatQueryUiStep\":\"think\"},\"status\":\"SUCCESS\",\"result\":{\"intentType\":\"data_question\",\"route\":\"standard_query\",\"understandingResult\":{\"originalQuestion\":\"查询电影数量\",\"understandingContent\":\"用户询问“查询电影数量”，这是一个数据查询问题，意图是获取数据库中电影（movie）的总数量。问题清晰明确，不涉及歧义。\"}}}},\"extraData\":{\"sessionId\":\"98468253-739c-4b08-b7f7-3b4eecddabfa\"},\"isCancel\":false}",
                    "Status": "FAILED",
                    "ChatType": "CHAT_QUERY_DATA",
                    "FeedbackRating": "",
                    "FeedbackContent": [],
                    "ReviewRequestStatus": "",
                    "Comment": ""
                }
            ]
        },
        "RequestId": "39474c77-ebff-4bfc-bd97-f45b7a490f90"
    }
}
```

