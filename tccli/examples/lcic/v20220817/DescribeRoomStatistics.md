**Example 1: 获取房间统计信息**

房间结束后获取房间相关的统计信息

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
        "RealStartTime": 1675677337,
        "RealEndTime": 1675677337,
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

**Example 2: 示例**

获取房间统计信息

Input: 

```
tccli lcic DescribeRoomStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PeakMemberNumber": 1,
        "MemberNumber": 1,
        "Total": 1,
        "MemberRecords": [
            {
                "UserId": "xx",
                "UserName": "xx",
                "PresentTime": 1,
                "Camera": 1,
                "Mic": 1,
                "Silence": 1,
                "AnswerQuestions": 1,
                "HandUps": 1,
                "FirstJoinTimestamp": 1,
                "LastQuitTimestamp": 1,
                "Rewords": 1
            }
        ],
        "RealStartTime": 1,
        "RealEndTime": 1,
        "RequestId": "xx"
    }
}
```

