**Example 1: 获取对话评论信息**



Input: 

```
tccli wedata ListChatBiDialogueComments --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --Key 488bcd5a1770120494578b241a4d1 \
    --RoomKey 803627528827023360
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Id": "338",
                    "Key": "5de96fdf1770123697308954773a6",
                    "OwnerUin": "700002164619",
                    "AppId": "260073493",
                    "WorkspaceId": "17678671667189298",
                    "Owner": "wedata30-test1@tencent.com",
                    "CreatedBy": "wedata30-test1@tencent.com",
                    "CreatedOn": "1770123697307",
                    "ModifiedBy": "wedata30-test1@tencent.com",
                    "ModifiedOn": "1770123697307",
                    "DialogueKey": "488bcd5a1770120494578b241a4d1",
                    "RoomKey": "803627528827023360",
                    "ChatTaskKey": "04e8687617701204945594888e03b",
                    "Comment": "1",
                    "CommentType": "REVIEW_REQUEST",
                    "Extra": "",
                    "OwnerRole": "MANAGE"
                },
                {
                    "Id": "337",
                    "Key": "3c5ec25f17701236346002d710809",
                    "OwnerUin": "700002164619",
                    "AppId": "260073493",
                    "WorkspaceId": "17678671667189298",
                    "Owner": "wedata30-test1@tencent.com",
                    "CreatedBy": "wedata30-test1@tencent.com",
                    "CreatedOn": "1770123634599",
                    "ModifiedBy": "wedata30-test1@tencent.com",
                    "ModifiedOn": "1770123634599",
                    "DialogueKey": "488bcd5a1770120494578b241a4d1",
                    "RoomKey": "803627528827023360",
                    "ChatTaskKey": "04e8687617701204945594888e03b",
                    "Comment": "异常",
                    "CommentType": "FEEDBACK_THUMBS_DOWN",
                    "Extra": "",
                    "OwnerRole": "MANAGE"
                },
                {
                    "Id": "336",
                    "Key": "2ea8b58a1770123624460c89a5509",
                    "OwnerUin": "700002164619",
                    "AppId": "260073493",
                    "WorkspaceId": "17678671667189298",
                    "Owner": "wedata30-test1@tencent.com",
                    "CreatedBy": "wedata30-test1@tencent.com",
                    "CreatedOn": "1770123624459",
                    "ModifiedBy": "wedata30-test1@tencent.com",
                    "ModifiedOn": "1770123624459",
                    "DialogueKey": "488bcd5a1770120494578b241a4d1",
                    "RoomKey": "803627528827023360",
                    "ChatTaskKey": "04e8687617701204945594888e03b",
                    "Comment": "",
                    "CommentType": "FEEDBACK_THUMBS_UP",
                    "Extra": "",
                    "OwnerRole": "MANAGE"
                }
            ]
        },
        "RequestId": "c51338d1-26df-49af-b104-a39c0acc240f"
    }
}
```

