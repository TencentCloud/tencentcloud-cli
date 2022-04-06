**Example 1: 查询外部联系人事件明细列表接口**



Input: 

```
tccli wav QueryExternalUserEventList --cli-unfold-argument  \
    --Cursor +1H24tK0tELjSiTOR10DzA== \
    --Limit 100 \
    --BeginTime 1647187200 \
    --EndTime 1647273600
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "EventCode": "ADD_EXTERNAL_CUSTOMER",
                "ExternalUserId": "woQIM2CwAA8BPLSVDDBZUYIlviX3_9DQ",
                "SalesId": "1323253932850728968",
                "EventTime": 1614923098
            }
        ],
        "RequestId": "4d48312c-a062-4875-a5d5-69f0f11baf96"
    }
}
```

