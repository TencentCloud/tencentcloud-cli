**Example 1: 查询ChatBi空间详情**



Input: 

```
tccli wedata GetChatBiSpace --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --Key 806111269456769024
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreatedBy": "700002164618",
            "CreatedOn": "1769999903992",
            "Description": "",
            "ExampleQuestionList": [],
            "ExecuteResourceId": "",
            "Favorite": false,
            "FileId": "806111269456769024",
            "Id": "419",
            "Key": "806111269456769024",
            "ModifiedBy": "700002164618",
            "ModifiedOn": "1769999903992",
            "Name": "ChatBI示例空间20260202_test1",
            "Owner": "700002164618",
            "PermissionInfo": {
                "AuthList": [
                    "chatbi_chatspace_view"
                ],
                "Permission": "MANAGE"
            },
            "WorkspaceId": "17623497097012366"
        },
        "RequestId": "4687ebce-c115-47c3-b596-a2a5c25f0848"
    }
}
```

