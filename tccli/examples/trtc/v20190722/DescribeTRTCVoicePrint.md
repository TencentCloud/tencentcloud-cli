**Example 1: 查询示例**



Input: 

```
tccli trtc DescribeTRTCVoicePrint --cli-unfold-argument  \
    --SdkAppId 1400123456 \
    --Offset 0 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "Message": "query voiceprint list successfully",
        "TotalCount": 4,
        "VoicePrintList": [
            {
                "CreateTime": "2026-04-24T01:45:35+08:00",
                "SpeakerId": "user4",
                "UpdateTime": "2026-04-24T01:45:35+08:00",
                "VoicePrintId": "19dbb727a75_f3be637f9fda4c10b5b466d28285efba"
            }
        ],
        "RequestId": "a14eb21b-8e78-46a0-baad-46e1ab952e95"
    }
}
```

