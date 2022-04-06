**Example 1: 查询外部联系人SaaS使用明细数据接口**



Input: 

```
tccli wav QueryCustomerEventDetailStatistics --cli-unfold-argument  \
    --Cursor xx \
    --Limit 0 \
    --BeginTime 1647273600 \
    --EndTime 1647573600
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "EventCode": "1000",
                "EventType": 1,
                "EventSource": 1,
                "MaterialType": 1,
                "MaterialId": 1348495383617208321,
                "ExternalUserId": "wmQIM2CwAAL1ZKqK-icQG9XAMa3AhP-A",
                "EventTime": 1647573600,
                "SalesId": 1323253932850728968
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

