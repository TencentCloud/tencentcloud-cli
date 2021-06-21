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
        "Status": "xx",
        "SentenceInfoSet": [
            {
                "SentenceId": 0,
                "PronFluency": 0.0,
                "SuggestedScore": 0.0,
                "PronCompletion": 0.0,
                "Words": [
                    {
                        "Word": "xx",
                        "MatchTag": 0,
                        "PhoneInfos": [
                            {
                                "Stress": true,
                                "ReferencePhone": "xx",
                                "MatchTag": 0,
                                "DetectedStress": true,
                                "Phone": "xx",
                                "MemBeginTime": 0,
                                "PronAccuracy": 0.0,
                                "MemEndTime": 0
                            }
                        ],
                        "PronFluency": 0.0,
                        "MemBeginTime": 0,
                        "ReferenceWord": "xx",
                        "PronAccuracy": 0.0,
                        "MemEndTime": 0
                    }
                ],
                "PronAccuracy": 0.0
            }
        ],
        "PronFluency": 0.3,
        "SessionId": "xx",
        "SuggestedScore": 0.0,
        "PronCompletion": 0.0,
        "Words": [
            {
                "Word": "xx",
                "MatchTag": 1,
                "PhoneInfos": [
                    {
                        "Stress": true,
                        "ReferencePhone": "xx",
                        "MatchTag": 0,
                        "DetectedStress": false,
                        "Phone": "xx",
                        "MemBeginTime": 1,
                        "PronAccuracy": 0.0,
                        "MemEndTime": 2
                    }
                ],
                "PronFluency": 0.3,
                "MemBeginTime": 1,
                "ReferenceWord": "xx",
                "PronAccuracy": 0.0,
                "MemEndTime": 2
            }
        ],
        "AudioUrl": "xx",
        "PronAccuracy": 0.0,
        "RequestId": "xx"
    }
}
```

