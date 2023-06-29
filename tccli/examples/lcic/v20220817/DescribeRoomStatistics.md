**Example 1: 示例**

获取房间统计信息示例

Input: 

```
tccli lcic DescribeRoomStatistics --cli-unfold-argument  \
    --RoomId 1 \
    --Page 1 \
    --Limit 1
```

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
                "Rewords": 1,
                "IPAddress": "xx",
                "Location": "xx",
                "Device": 0
            }
        ],
        "RealStartTime": 1,
        "RealEndTime": 1,
        "MessageCount": 1,
        "MicCount": 1,
        "RequestId": "xx"
    }
}
```

