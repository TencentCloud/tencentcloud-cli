**Example 1: 查询外部联系人列表**



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
                "ExternalUserId": "wmpqy2CAAATGwpQTxuU1IUfoiOFH2cXA",
                "DepartmentIdList": [
                    0,
                    1
                ]
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

