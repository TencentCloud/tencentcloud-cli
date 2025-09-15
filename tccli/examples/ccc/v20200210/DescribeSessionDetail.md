**Example 1: 查询通话详情示例**

查询通话详情示例

Input: 

```
tccli ccc DescribeSessionDetail --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId 0f507d5d-e1e4-436e-a655-1d6c75a79b4f \
    --StartTimestamp 1756372067 \
    --EndTimestamp 1756893037
```

Output: 
```
{
    "Response": {
        "AcceptTimestamp": 1756892204,
        "AsrURL": "https://tccc.qcloud.com/tcccadmin/cdr/getAsrText?key=PEbNJ4mQ723VpLFHvMinns4n8Pnq1nmySYbmD7tljzGXyrb6jvtOBGbrQBAg%3D%3D-k-fKVP3WIlGpg8m9LMW4jEkQ%3D%3D-k-Hz86ZdIwexo5JKCsB%2BGeybDY6nqSjwcpbXifo%2B%2FNDf9LzO9%IZHUrajgyWkRDUWxLNWxVQkF3N0N6V1VKZnlhVWljWmNVV01HR2NPL2NyRlBKeW92NFcwV0ZvUklibFl1RExOdkFaSkFONmlqOWxrQWlCMTFrNmNZWVgrQWdObEJ3OTZzTjJwTWk0UEZ2cS9tZXc9PSIsIm5vbmNlIjoiMDd1aFNLRDFmSTV4enQzNyX9",
        "CallType": 1,
        "Callee": "0086158xxxxxxxx",
        "Caller": "00860755xxxxxxxx",
        "CustomRecordURL": "https://example.cos.ap-guangzhou.tencentcos.cn/record/2025/09/03/17/1756892231_f460fff5-0cad-8424-e904ef6a76d2.mp3",
        "EndStatus": 1,
        "EndedTimestamp": 1756892230,
        "Events": [
            {
                "EventType": "StaffHold",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892209
            },
            {
                "EventType": "StaffUnhold",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892217
            },
            {
                "EventType": "StaffMute",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892220
            },
            {
                "EventType": "StaffUnmute",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892224
            }
        ],
        "HungUpSide": "user",
        "IVRKeyPressed": [],
        "PostIVRKeyPressed": [],
        "QueuedSkillGroupId": 0,
        "QueuedSkillGroupName": "",
        "QueuedTimestamp": 0,
        "RecordURL": "https://tccc.qcloud.com/tcccadmin/getRecord/PEbNJ4mQ723VpLFHvMinns4n8Pnq1nmySYbmD7tljzGXyrb6jDk+I%+Fd6MhhwvtOBGbrQBAg==-k-fKVP3WIlGpg8m9LMW4jEkQ==-k-nhmzd124T8YIkIsnUjieNBmvkGzu6mYJxMPYpb9zwZc4bsUdV%=/eyJ0b2tlbklkRW52IjoicW5icGdyOG1NaTdWOFo2c3F3N3UxSDdDVUYzYi9ZRzhqUE1heGJRY0pFdG9tZkJmNW9CNDdpNG1ZaWIzMXFNZW1XNzh2MWdqdm4wUE9JRkoxMFdRLzgvTXFDVEtzSFlOdVIzYTZPN295VDUvaHdoU2lXVVZNWlNOdlJTdXk5UWEwUGZjZ0RQbFo4Z0RubVd3SzNLTld0NTdTVmxQS3lVdEVEMGtCeGtnZzlIbHpDSnN3VllkN290R1ZTVjBpVHQ5eTRPRll4a0ErL2ZHYXpUMEpvcWZyckhtcVJVbnRYSTNQazJ4N0RPSTdvZ1F6VTNwUlBTTXNPU1hhNUF2S0g3YVRTRk44Yk9lTHowcmtTMXlFSVVRIiwibm9uY2UiOiJvVlBmQW9yU1NqMDNwWEZTIn0=/000-2529533707-11368-dd792000e656498092f0672dd10f1954-000-1756892321.mp3",
        "RequestId": "d6053004-779e-4cea-bbff-aa689b5fb9ff",
        "RingTimestamp": 1756892201,
        "ServeParticipants": [
            {
                "AcceptTimestamp": 1756892204,
                "CustomRecordURL": "https://example.cos.ap-guangzhou.tencentcos.cn/record/2025/09/03/17/1756892231_8a76adc6-e70c-459d-8921-56c88d91f840.mp3",
                "EndStatusString": "ok",
                "EndedTimestamp": 1756892230,
                "Mail": "foo@tencent.com",
                "Phone": "",
                "RecordId": "8a76adc6-e70c-459d-8921-56c88d91f840",
                "RecordURL": "https://tccc.qcloud.com/tcccadmin/getRecord/PEbNJ4mQ723VpLFHvMinns4n8Pnq1nmySYbmD7tljzGXyrb6jDk+I%2Fte3zvgZBju2cQ+Fd6MhhwvtOBGbrQBAg==-k-fKVP3WIlGpg8m9LMW4jEkQ==-k-nhmzd124T8YIkIsnUjieNBmvkGzu6mYJxMPYpb9zwZc4bsUdV%2FRydVMnwbuKd1DLNvTC8LpUTz2ToslvXs4onjeAOlY=/eyJ0b2tlbklkRW52IjoiSjlkVXNhWlB4cGRydEJydEN6UEQ0dVBZNVBKTTM3ZjdoWjA3N05Ob3BFaVRQenlkVjRZK2tQNmpPWlN0Vjh2VFg1ZGJNcUFZK0RCckhMbHRnMks5ZGw1cWQwRzN5VURBQmdKeTZSYnVvcjYzejNTeXZxWHhZNGpEQUdYRkJ6NU9lMWZYbFB6akh0TEhRMFJhL0VvcTFlR1g2VDhiejVUUVJLNkk2Q3NMNDRRSUsvcDZ0QmlLV08xLzFCOW9RNXZIbk1zZmpzYXViem1Zb05RengvL1VuMERXcm9qeHNLby9RYzdLejhjVEtqZGE5dGtSVlJhK1hGZU90Q2pEMUNsbmdqYUhWd0pxVDNaQjMxMlZYeWNaIiwibm9uY2UiOiJWZkNxbU5teG1mcjVFeW1QIn0=/000-3989151499-12368-6808000033894582a618470286620405-000-1756892101.mp3",
                "RingTimestamp": 1756892198,
                "Sequence": 0,
                "SkillGroupId": 2522,
                "SkillGroupName": "foo-tel",
                "StartTimestamp": 1756892198,
                "TransferFrom": "",
                "TransferFromType": "",
                "TransferTo": "",
                "TransferToType": "",
                "Type": "staffSeat"
            }
        ],
        "StaffUserId": "foo@tencent.com",
        "StartTimeStamp": 1756892198,
        "UUI": "",
        "VoicemailAsrURL": [],
        "VoicemailRecordURL": []
    }
}
```

