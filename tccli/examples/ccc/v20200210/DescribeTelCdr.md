**Example 1: 获取电话话单示例**



Input: 

```
tccli ccc DescribeTelCdr --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --StartTimeStamp 1590547606 \
    --EndTimeStamp 1590147606 \
    --Limit 0 \
    --Offset 0 \
    --PageSize 10 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TelCdrs": [
            {
                "ProtectedCaller": "xx",
                "EndStatus": 1,
                "SessionId": "xx",
                "ProtectedCallee": "xx",
                "Direction": 0,
                "StartTimestamp": 1590547606,
                "HungUpSide": "xx",
                "ServeParticipants": [
                    {
                        "TransferTo": "xx",
                        "EndStatusString": "xx",
                        "RecordURL": "xx",
                        "TransferToType": "xx",
                        "AcceptTimestamp": 0,
                        "RecordId": "xx",
                        "TransferFrom": "xx",
                        "EndedTimestamp": 0,
                        "Sequence": 0,
                        "Phone": "xx",
                        "SkillGroupName": "xx",
                        "Mail": "xx",
                        "RingTimestamp": 0,
                        "Type": "xx",
                        "StartTimestamp": 0,
                        "SkillGroupId": 0
                    }
                ],
                "PostIVRKeyPressed": [
                    {
                        "Key": "xx",
                        "Label": "xx"
                    }
                ],
                "EndStatusString": "xx",
                "QueuedSkillGroupId": 100,
                "RingTimestamp": 1590547606,
                "AcceptTimestamp": 1590547606,
                "EndedTimestamp": 1590547606,
                "Caller": "xx",
                "CallerLocation": "xx",
                "Time": 1590547606,
                "Callee": "xx",
                "SeatUser": {
                    "Name": "xx",
                    "Phone": "xx",
                    "UserId": "xx",
                    "Nick": "xx",
                    "StaffNumber": "xx",
                    "Mail": "xx",
                    "SkillGroupNameList": [
                        "xx"
                    ]
                },
                "RecordURL": "xx",
                "QueuedTimestamp": 1610627284,
                "IVRDuration": 5,
                "SkillGroup": "xx",
                "Duration": 60,
                "IVRKeyPressed": [
                    "5"
                ],
                "SkillGroupId": 100
            },
            {
                "ProtectedCaller": "xx",
                "EndStatus": 1,
                "SessionId": "xx",
                "ProtectedCallee": "xx",
                "Direction": 0,
                "StartTimestamp": 1590547630,
                "HungUpSide": "xx",
                "ServeParticipants": [
                    {
                        "TransferTo": "xx",
                        "RecordURL": "xx",
                        "TransferToType": "xx",
                        "AcceptTimestamp": 0,
                        "RecordId": "xx",
                        "TransferFrom": "xx",
                        "EndedTimestamp": 0,
                        "Sequence": 0,
                        "Phone": "xx",
                        "EndStatusString": "xx",
                        "SkillGroupName": "xx",
                        "Mail": "xx",
                        "RingTimestamp": 0,
                        "Type": "xx",
                        "StartTimestamp": 0,
                        "SkillGroupId": 0
                    }
                ],
                "PostIVRKeyPressed": [
                    {
                        "Key": "xx",
                        "Label": "xx"
                    }
                ],
                "EndStatusString": "xx",
                "QueuedSkillGroupId": 100,
                "RingTimestamp": 1590547606,
                "AcceptTimestamp": 1590547606,
                "EndedTimestamp": 1590547606,
                "Caller": "xx",
                "CallerLocation": "xx",
                "Time": 1590547630,
                "Callee": "xx",
                "SeatUser": {
                    "Name": "xx",
                    "Nick": "xx",
                    "UserId": "xx",
                    "Phone": "xx",
                    "StaffNumber": "xx",
                    "Mail": "xx",
                    "SkillGroupNameList": [
                        "xx"
                    ]
                },
                "RecordURL": "xx",
                "QueuedTimestamp": 1610627284,
                "IVRDuration": 5,
                "SkillGroup": "xx",
                "Duration": 62,
                "IVRKeyPressed": [
                    "5"
                ],
                "SkillGroupId": 100
            }
        ],
        "RequestId": "xx"
    }
}
```

