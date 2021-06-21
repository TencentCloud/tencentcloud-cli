**Example 1: 客户列表**



Input: 

```
tccli wav QueryExternalContactList --cli-unfold-argument  \
    --Cursor xxxx \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "xxx",
        "PageData": [
            {
                "SalesName": "",
                "UserId": "xxx",
                "ExternalUserId": "xxx"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

