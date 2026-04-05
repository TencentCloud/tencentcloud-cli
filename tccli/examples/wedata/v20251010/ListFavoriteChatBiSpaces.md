**Example 1: 查询ChatBI空间收藏列表**



Input: 

```
tccli wedata ListFavoriteChatBiSpaces --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --TokenPageRequest.MaxResults 30
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1767669668365",
                    "CreatedUser": "wedata30-dev@tencent.com",
                    "Description": "",
                    "Favorite": true,
                    "FileId": "",
                    "Id": "344",
                    "Key": "796337551086989312",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1767669668365",
                    "ModifiedUser": "wedata30-dev@tencent.com",
                    "Name": "新空间_2026-01-06 11:21:04",
                    "Owner": "700002164618",
                    "OwnerUser": "wedata30-dev@tencent.com",
                    "WorkspaceId": "17622177773248536"
                }
            ],
            "TokenPageResponse": {
                "NextPageToken": ""
            }
        },
        "RequestId": "18c8b7f4-378c-4dbc-94ba-f861d777c47d"
    }
}
```

