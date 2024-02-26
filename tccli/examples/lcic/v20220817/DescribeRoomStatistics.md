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
                "UserId": "90813",
                "UserName": "Name",
                "PresentTime": 1,
                "Camera": 1,
                "Mic": 1,
                "Silence": 1,
                "AnswerQuestions": 1,
                "HandUps": 1,
                "FirstJoinTimestamp": 1,
                "LastQuitTimestamp": 1,
                "Rewords": 1,
                "IPAddress": "1.1.1.1",
                "Location": "country",
                "Device": 0,
                "PerMemberMicCount": 0,
                "PerMemberMessageCount": 0,
                "Role": 1,
                "GroupId": "abc",
                "SubGroupId": [
                    "abc"
                ],
                "Stage": 0,
                "CurrentState": 1
            }
        ],
        "RealStartTime": 1,
        "RealEndTime": 1,
        "MessageCount": 1,
        "MicCount": 1,
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

