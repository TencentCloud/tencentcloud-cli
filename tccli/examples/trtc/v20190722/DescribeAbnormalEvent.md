**Example 1: 查询异常体验事件**



Input: 

```
tccli trtc DescribeAbnormalEvent --cli-unfold-argument  \
    --StartTime 1590065777 \
    --SdkAppId 1400188366 \
    --EndTime 1590065877 \
    --RoomId 461
```

Output: 
```
{
    "Response": {
        "AbnormalExperienceList": [
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448600,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachili1",
                "RoomId": "461",
                "EventTime": 1592448600,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448660,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448720,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448780,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448600,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2021,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2022,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2011,
                        "PeerId": "itachili1"
                    },
                    {
                        "AbnormalEventId": 2012,
                        "PeerId": "itachili1"
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448600,
                "ExperienceId": 5,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448660,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2021,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2022,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448660,
                "ExperienceId": 5,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448720,
                "ExperienceId": 4,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2021,
                        "PeerId": ""
                    },
                    {
                        "AbnormalEventId": 2022,
                        "PeerId": ""
                    }
                ]
            },
            {
                "UserId": "itachi3",
                "RoomId": "461",
                "EventTime": 1592448720,
                "ExperienceId": 5,
                "AbnormalEventList": [
                    {
                        "AbnormalEventId": 2014,
                        "PeerId": ""
                    }
                ]
            }
        ],
        "Total": 11,
        "RequestId": "75a3a17f-ca35-4cc8-b42f-2ebb8903b6a7"
    }
}
```

