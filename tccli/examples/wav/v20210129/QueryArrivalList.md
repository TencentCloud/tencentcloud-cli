**Example 1: 查询指定时间范围内发生过到店的潜客到店信息**

查询指定时间范围内发生过到店的潜客到店信息

Input: 

```
tccli wav QueryArrivalList --cli-unfold-argument  \
    --Cursor 2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw \
    --Limit 100 \
    --BeginTime 1618322621 \
    --EndTime 1618322621
```

Output: 
```
{
    "Response": {
        "NextCursor": "2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw",
        "PageData": [
            {
                "ClueId": 1348080105398452200,
                "CustomerId": 1348080105398452200,
                "UserName": "张三",
                "Phone": "134xxxx4321",
                "FirstArrival": 1,
                "ArrivalTime": 1618322621,
                "EventType": 1,
                "EventTypeName": "首次到店",
                "FollowRecord": ""
            }
        ],
        "HasMore": 1,
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

