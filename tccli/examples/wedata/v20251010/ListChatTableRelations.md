**Example 1: 关联列表**

关联列表

Input: 

```
tccli wedata ListChatTableRelations --cli-unfold-argument  \
    --WorkspaceId 1 \
    --RoomKey 1 \
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
                    "Id": "0",
                    "Key": "",
                    "ModifiedBy": "",
                    "ModifiedOn": "0",
                    "Owner": "",
                    "OwnerUin": "",
                    "RelationType": "",
                    "WorkspaceId": ""
                }
            ]
        },
        "RequestId": "1329f4bf-a0c5-49e9-9cd2-657ef4c2451f"
    }
}
```

