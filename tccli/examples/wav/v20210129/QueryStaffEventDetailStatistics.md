**Example 1: 查询企业成员SaaS使用明细数据接口**



Input: 

```
tccli wav QueryStaffEventDetailStatistics --cli-unfold-argument  \
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
                "EventTime": 1647573600,
                "SalesId": 1323253932850728968
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

