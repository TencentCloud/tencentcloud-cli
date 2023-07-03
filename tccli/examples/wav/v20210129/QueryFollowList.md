**Example 1: 查询指定时间范围内发生过跟进的潜客信息**

查询指定时间范围内发生过跟进的潜客信息

Input: 

```
tccli wav QueryFollowList --cli-unfold-argument  \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU= \
    --Limit 100 \
    --BeginTime 1647187200 \
    --EndTime 1647187200
```

Output: 
```
{
    "Response": {
        "NextCursor": "sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU=",
        "PageData": [
            {
                "ClueId": 1348080105398452200,
                "CustomerId": 1348080105398452200,
                "UserName": "张三",
                "Phone": "134xxxx1234",
                "IsOverdue": 0,
                "OverdueTime": 1618322621,
                "EventType": 1,
                "EventTypeName": "逾期",
                "FollowWayType": "1",
                "FollowWayName": "自然逾期",
                "FollowTime": 1618322621,
                "NextFollowTime": 1618322621,
                "FollowRecord": "abc"
            }
        ],
        "HasMore": 1,
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

