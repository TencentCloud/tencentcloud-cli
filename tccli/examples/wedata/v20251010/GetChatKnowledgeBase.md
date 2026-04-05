**Example 1: 查询知识库**

查询知识库

Input: 

```
tccli wedata GetChatKnowledgeBase --cli-unfold-argument  \
    --WorkspaceId asdf \
    --RoomKey sadf \
    --KnowledgeBaseKey sdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "",
            "CreatedBy": "",
            "CreatedOn": "0",
            "Enable": 0,
            "ErrorInfo": "",
            "Id": "0",
            "Key": "",
            "KnowledgeNum": 0,
            "ModifiedBy": "",
            "ModifiedOn": "0",
            "Name": "",
            "Owner": "",
            "OwnerUin": "",
            "RoomKey": "",
            "Scope": "",
            "Status": "",
            "TableKeyList": [],
            "TableNameList": [],
            "Type": "",
            "WorkspaceId": ""
        },
        "RequestId": "e97a8a1a-963c-4977-ab6d-75e2e09d24c3"
    }
}
```

