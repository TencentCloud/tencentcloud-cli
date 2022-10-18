**Example 1: 获取房间统计信息**



Input: 

```
tccli lcic DescribeRoomStatistics --cli-unfold-argument  \
    --RoomId 123 \
    --Page 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "MemberNumber": 1,
        "Total": 1,
        "PeakMemberNumber": 1,
        "RequestId": "xx",
        "MemberRecords": [
            {
                "UserName": "xx",
                "Mic": 1,
                "UserId": "xx",
                "Rewords": 1,
                "AnswerQuestions": 1,
                "HandUps": 1,
                "Camera": 1,
                "FirstJoinTimestamp": 1,
                "LastQuitTimestamp": 1,
                "PresentTime": 1,
                "Silence": 1
            }
        ]
    }
}
```

