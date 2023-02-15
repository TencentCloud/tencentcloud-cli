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

