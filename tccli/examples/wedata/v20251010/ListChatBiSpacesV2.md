**Example 1: 获取ChatBI空间列表**



Input: 

```
tccli wedata ListChatBiSpacesV2 --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --TokenPageRequest.MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1769766133971",
                    "CreatedUser": "wedata30-dev@tencent.com",
                    "Description": "",
                    "ExampleQuestionList": [],
                    "ExecuteResourceId": "res-8be1b918",
                    "Favorite": false,
                    "FileId": "805130767391080448",
                    "Id": "415",
                    "Key": "805130767391080448",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1769766133971",
                    "ModifiedUser": "wedata30-dev@tencent.com",
                    "Name": "ChatBI示例空间20260130_test1",
                    "Owner": "700002164618",
                    "OwnerUser": "wedata30-dev@tencent.com",
                    "WorkspaceId": "17622177773248536"
                }
            ],
            "TokenPageResponse": {
                "NextPageToken": "1"
            }
        },
        "RequestId": "120ec93b-3bd0-4c45-9cbd-f972d8402b8f"
    }
}
```

