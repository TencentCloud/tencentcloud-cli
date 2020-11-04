**Example 1: 查询详细事件**

查询用户某次通话内的进退房，视频开关等详细事件

Input: 

```
tccli trtc DescribeDetailEvent --cli-unfold-argument  \
    --CommId 1400188366_3568_1588055615\
    --StartTime 1588055615\
    --EndTime 1588058615\
    --UserId user_66319581\
    --RoomId 1711
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975272790,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "hyder11"
            },
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975212877,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "user_20453511"
            },
            {
                "Content": [
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32769,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32791,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32768,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32788,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    },
                    {
                        "Type": 0,
                        "Time": 1589975202782,
                        "EventId": 32793,
                        "ParamOne": -1,
                        "ParamTwo": -1
                    }
                ],
                "PeerId": "user_66319581"
            }
        ],
        "RequestId": "093bffd3-9d27-45ca-8410-c61c0e4cdcb8"
    }
}
```

