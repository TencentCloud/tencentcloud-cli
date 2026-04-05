**Example 1: 查询sql知识列表**

查询sql知识列表

Input: 

```
tccli wedata ListChatSqlKnowledge --cli-unfold-argument  \
    --WorkspaceId asdf \
    --RoomKey ss \
    --PageRequest.PageNumber 11 \
    --PageRequest.PageSize 11 \
    --PageRequest.AllPage True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppId": "",
                    "Comment": "",
                    "Content": "",
                    "CreatedBy": "",
                    "CreatedOn": "0",
                    "Id": "0",
                    "Key": "",
                    "KnowledgeType": "",
                    "ModifiedBy": "",
                    "ModifiedOn": "0",
                    "Name": "",
                    "Owner": "",
                    "OwnerUin": "",
                    "WorkspaceId": ""
                }
            ]
        },
        "RequestId": "6630656c-86a4-4274-aa46-ff227ed41e59"
    }
}
```

