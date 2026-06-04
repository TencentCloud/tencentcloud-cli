**Example 1: 获取Skills模式的conversation**



Input: 

```
tccli adp DescribeConversation --cli-unfold-argument  \
    --ConversationId 4abd149a-e010-4a6c-bc52-1132658f149d \
    --Type 2 \
    --AppKey 1 \
    --ShareCode 1 \
    --UserId 1 \
    --LoginSubAccountUin 700001046587 \
    --LoginUin 700001046587
```

Output: 
```
{
    "Response": {
        "AppId": "2049746910862560576",
        "ConversationId": "4abd149a-e010-4a6c-bc52-1132658f149d",
        "CreateTime": "2026-04-30T15:05:27+08:00",
        "Type": 2,
        "UpdateTime": "2026-04-30T16:01:05+08:00",
        "Workspace": {
            "StorageType": "sandbox_e2b",
            "WorkspaceId": "6576c839-839c-4a54-b820-408aec31dbe0"
        },
        "RequestId": "7fcd93a2-6fe4-4809-9c9e-d03dad2a0aaf"
    }
}
```

