**Example 1: 获取当前房间的成员列表**

获取当前房间的成员列表。房间结束或过期后无法使用

Input: 

```
tccli lcic DescribeCurrentMemberList --cli-unfold-argument  \
    --RoomId 123 \
    --Page 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "MemberRecords": [
            {
                "UserId": "109912",
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
                "Location": "abc",
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
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

