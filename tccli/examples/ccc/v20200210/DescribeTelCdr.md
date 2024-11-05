**Example 1: 获取电话话单示例**



Input: 

```
tccli ccc DescribeTelCdr --cli-unfold-argument  \
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
        "TotalCount": 1,
        "TelCdrList": [
            {
                "AcceptTimestamp": 1729756307,
                "AsrStatus": "Complete",
                "AsrUrl": "https://xxxxxx",
                "Callee": "00860200000000",
                "Caller": "0086075500000",
                "CallerLocation": "广东深圳固话",
                "CustomRecordURL": "https://xxxxxxxx.mp3",
                "Direction": 0,
                "Duration": 8,
                "EndStatus": 1,
                "EndStatusString": "ok",
                "EndedTimestamp": 1729756315,
                "HungUpSide": "seat",
                "IVRDuration": 15,
                "IVRKeyPressed": [
                    "香蕉"
                ],
                "IVRKeyPressedEx": [
                    {
                        "Key": "香蕉",
                        "Label": "香蕉",
                        "NodeLabel": "语音识别导航",
                        "OriginalContent": "香蕉。",
                        "TTSPrompt": "输入您喜欢吃的水果",
                        "Timestamp": 1729756303211
                    }
                ],
                "PostIVRKeyPressed": [
                    {
                        "Key": "1",
                        "Label": "不满意",
                        "NodeLabel": "",
                        "OriginalContent": "",
                        "TTSPrompt": "",
                        "Timestamp": 0
                    }
                ],
                "ProtectedCallee": "",
                "ProtectedCaller": "",
                "QueuedSkillGroupId": 2522,
                "QueuedSkillGroupName": "test-tel",
                "QueuedTimestamp": 1729756306,
                "RecordId": "e9fdbff5-2e35-4480-83f7-81917e723fa5",
                "RecordURL": "https://xxxxxxx.mp3",
                "Remark": "skillGroupId--34588",
                "RingTimestamp": 1729756306,
                "SeatUser": {
                    "Mail": "xxxxxxx@tencent.com",
                    "Name": "xiaoming",
                    "Nick": "guanjia",
                    "Phone": "00861580000000",
                    "SkillGroupNameList": [
                        "1539",
                        "2522",
                        "3551"
                    ],
                    "StaffNumber": "20012",
                    "UserId": "xxxxxxx@tencent.com"
                },
                "ServeParticipants": [
                    {
                        "AcceptTimestamp": 1729756306,
                        "CustomRecordURL": "https://xxxxx.mp3",
                        "EndStatusString": "ok",
                        "EndedTimestamp": 1729756312,
                        "Mail": "xxxxxx@tencent.com",
                        "Phone": "",
                        "RecordId": "96eaa575-be4c-48f1-99b8-9722f2f816ec",
                        "RecordURL": "https://xxxxxx.mp3",
                        "RingTimestamp": 1729756306,
                        "Sequence": 0,
                        "SkillGroupId": 2522,
                        "SkillGroupName": "test-tel",
                        "StartTimestamp": 1729756306,
                        "TransferFrom": "",
                        "TransferFromType": "",
                        "TransferTo": "",
                        "TransferToType": "",
                        "Type": "staffSeat"
                    }
                ],
                "SessionId": "0955de87-c86d-4457-aac2-bee3d0a0b67a",
                "SkillGroup": "test-tel",
                "SkillGroupId": 2522,
                "StartTimestamp": 1729756291,
                "Time": 1729756291,
                "UUI": "",
                "Uui": "",
                "VoicemailAsrURL": [],
                "VoicemailRecordURL": []
            }
        ],
        "RequestId": "abc"
    }
}
```

