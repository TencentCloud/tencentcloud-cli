**Example 1: 传输语音进行发音评估**

传输语音进行发音评估

Input: 

```
tccli soe TransmitOralProcess --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --VoiceFileType 1 \
    --SeqId 1 \
    --VoiceEncodeType 1 \
    --IsEnd 0 \
    --UserVoiceData VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5
```

Output: 
```
{
    "Response": {
        "PronAccuracy": 65,
        "PronFluency": 0.3,
        "PronCompletion": 1,
        "SuggestedScore": 65,
        "RequestId": "xxxxxxx",
        "Words": [
            {
                "MemBeginTime": 1,
                "MemEndTime": 2,
                "PronAccuracy": 65,
                "PronFluency": 0.3,
                "Word": "xxx",
                "MatchTag": 1,
                "PhoneInfos": [
                    {
                        "MemBeginTime": 1,
                        "MemEndTime": 2,
                        "PronAccuracy": 52,
                        "Phone": "b",
                        "Stress": true,
                        "DetectedStress": false
                    }
                ]
            }
        ]
    }
}
```

