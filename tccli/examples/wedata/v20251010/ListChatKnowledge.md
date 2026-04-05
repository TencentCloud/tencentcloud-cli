**Example 1: 查询知识列表**

查询知识列表

Input: 

```
tccli wedata ListChatKnowledge --cli-unfold-argument  \
    --WorkspaceId asdfa \
    --RoomKey fafafw \
    --KnowledgeBaseKey eafds \
    --PageRequest.PageNumber 11 \
    --PageRequest.PageSize 11 \
    --PageRequest.AllPage False
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppId": "",
                    "CreatedBy": "",
                    "CreatedByName": "",
                    "CreatedOn": "0",
                    "Explanation": "",
                    "Id": "0",
                    "Key": "",
                    "ModifiedBy": "",
                    "ModifiedByName": "",
                    "ModifiedOn": "0",
                    "Noun": "",
                    "Owner": "",
                    "OwnerUin": "",
                    "WorkspaceId": ""
                }
            ]
        },
        "RequestId": "c9162e42-fdd4-44b2-b3bb-d9c114c1ed50"
    }
}
```

