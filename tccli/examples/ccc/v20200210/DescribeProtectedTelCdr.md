**Example 1: 获取主被叫受保护的电话话单示例**



Input: 

```
tccli ccc DescribeProtectedTelCdr --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --StartTimeStamp 1590547606 \
    --EndTimeStamp 1590147606 \
    --PageSize 10 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TelCdrList": [
            {
                "ProtectedCaller": "abc",
                "EndStatus": 1,
                "SessionId": "abc",
                "CustomRecordURL": "abc",
                "SkillGroupId": 100,
                "Direction": 0,
                "StartTimestamp": 1590547606,
                "AsrUrl": "abc",
                "HungUpSide": "abc",
                "ServeParticipants": [
                    {
                        "TransferTo": "abc",
                        "TransferFromType": "abc",
                        "EndStatusString": "abc",
                        "RecordURL": "abc",
                        "TransferToType": "abc",
                        "AcceptTimestamp": 0,
                        "RecordId": "abc",
                        "TransferFrom": "abc",
                        "EndedTimestamp": 0,
                        "Sequence": 0,
                        "Phone": "abc",
                        "SkillGroupName": "abc",
                        "Mail": "abc",
                        "RingTimestamp": 0,
                        "Type": "abc",
                        "StartTimestamp": 0,
                        "CustomRecordURL": "abc",
                        "SkillGroupId": 0
                    }
                ],
                "PostIVRKeyPressed": [
                    {
                        "Key": "abc",
                        "Label": "abc"
                    }
                ],
                "EndStatusString": "abc",
                "UUI": "abc",
                "QueuedSkillGroupId": 100,
                "RingTimestamp": 1590547606,
                "AcceptTimestamp": 1590547606,
                "EndedTimestamp": 1590547606,
                "Caller": "",
                "CallerLocation": "abc",
                "Time": 1590547606,
                "Callee": "",
                "SeatUser": {
                    "Name": "abc",
                    "Phone": "abc",
                    "UserId": "abc",
                    "Nick": "abc",
                    "StaffNumber": "abc",
                    "Mail": "abc",
                    "SkillGroupNameList": [
                        "abc"
                    ]
                },
                "RecordURL": "abc",
                "RecordId": "abc",
                "QueuedTimestamp": 1610627284,
                "ProtectedCallee": "abc",
                "IVRDuration": 5,
                "SkillGroup": "abc",
                "Duration": 60,
                "IVRKeyPressed": [
                    "5"
                ],
                "IVRKeyPressedEx": [
                    {
                        "Key": "abc",
                        "Label": "abc"
                    }
                ],
                "QueuedSkillGroupName": "abc",
                "Remark": "abc",
                "VoicemailRecordURL": [
                    "abc"
                ]
            },
            {
                "ProtectedCaller": "abc",
                "EndStatus": 1,
                "SessionId": "abc",
                "CustomRecordURL": "abc",
                "SkillGroupId": 100,
                "Direction": 0,
                "StartTimestamp": 1590547630,
                "AsrUrl": "abc",
                "HungUpSide": "abc",
                "ServeParticipants": [
                    {
                        "TransferTo": "abc",
                        "TransferFromType": "abc",
                        "RecordURL": "abc",
                        "TransferToType": "abc",
                        "AcceptTimestamp": 0,
                        "RecordId": "abc",
                        "TransferFrom": "abc",
                        "EndedTimestamp": 0,
                        "Sequence": 0,
                        "Phone": "abc",
                        "EndStatusString": "abc",
                        "SkillGroupName": "abc",
                        "Mail": "abc",
                        "RingTimestamp": 0,
                        "Type": "abc",
                        "StartTimestamp": 0,
                        "CustomRecordURL": "abc",
                        "SkillGroupId": 0
                    }
                ],
                "PostIVRKeyPressed": [
                    {
                        "Key": "abc",
                        "Label": "abc"
                    }
                ],
                "EndStatusString": "abc",
                "UUI": "abc",
                "QueuedSkillGroupId": 100,
                "RingTimestamp": 1590547606,
                "AcceptTimestamp": 1590547606,
                "EndedTimestamp": 1590547606,
                "Caller": "",
                "CallerLocation": "abc",
                "Time": 1590547630,
                "Callee": "",
                "SeatUser": {
                    "Name": "abc",
                    "Nick": "abc",
                    "UserId": "abc",
                    "Phone": "abc",
                    "StaffNumber": "abc",
                    "Mail": "abc",
                    "SkillGroupNameList": [
                        "abc"
                    ]
                },
                "RecordURL": "abc",
                "RecordId": "abc",
                "QueuedTimestamp": 1610627284,
                "ProtectedCallee": "abc",
                "IVRDuration": 5,
                "SkillGroup": "abc",
                "Duration": 62,
                "IVRKeyPressed": [
                    "5"
                ],
                "IVRKeyPressedEx": [
                    {
                        "Key": "abc",
                        "Label": "abc"
                    }
                ],
                "QueuedSkillGroupName": "abc",
                "Remark": "abc",
                "VoicemailRecordURL": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

