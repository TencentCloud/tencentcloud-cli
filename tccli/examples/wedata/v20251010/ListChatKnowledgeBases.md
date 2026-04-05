**Example 1: 知识库列表**

知识库列表

Input: 

```
tccli wedata ListChatKnowledgeBases --cli-unfold-argument  \
    --WorkspaceId asdfaf \
    --RoomKey afasdf \
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
                    "CreatedBy": "",
                    "CreatedOn": "0",
                    "Enable": 0,
                    "Id": "0",
                    "Key": "",
                    "KnowledgeBaseKey": "",
                    "ModifiedBy": "",
                    "ModifiedOn": "0",
                    "Name": "",
                    "Owner": "",
                    "OwnerUin": "",
                    "Scope": "",
                    "TableNameList": [],
                    "Type": "",
                    "WorkspaceId": ""
                }
            ]
        },
        "RequestId": "62835989-ff76-49a0-9229-c1e75556836c"
    }
}
```

