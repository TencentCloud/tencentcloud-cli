**Example 1: 客户列表**



Input: 

```
tccli wav QueryExternalContactList --cli-unfold-argument  \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU=",
        "PageData": [
            {
                "SalesName": "杨过",
                "UserId": "YangGuo",
                "ExternalUserId": "wmpqy2CAAATGwpQTxuU1IUfoiOFH2cXA"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

