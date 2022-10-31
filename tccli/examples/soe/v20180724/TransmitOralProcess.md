**Example 1: 传输语音进行发音评估**

传输语音进行发音评估

Input: 

```
tccli soe TransmitOralProcess --cli-unfold-argument  \
    --VoiceEncodeType 1 \
    --UserVoiceData VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5 \
    --IsEnd 0 \
    --VoiceFileType 1 \
    --SessionId stress_test_956938 \
    --SeqId 1
```

Output: 
```
{
    "Response": {
        "SuggestedScore": 99.52305,
        "PronAccuracy": 99.52305,
        "PronFluency": 0.93664527,
        "PronCompletion": 1,
        "RequestId": "1067cb5d-****-****-b1c6-6b*****72a0e",
        "RefTextId": 0,
        "KeyWordHits": [
            0.0
        ],
        "UnKeyWordHits": [
            0.0
        ],
        "Words": [
            {
                "KeywordTag": 0,
                "MemBeginTime": 2330,
                "MemEndTime": 3170,
                "PronAccuracy": 99.52305,
                "PronFluency": 0.93664527,
                "ReferenceWord": "",
                "Word": "thankyou",
                "MatchTag": 0,
                "PhoneInfos": [
                    {
                        "MemBeginTime": 2330,
                        "MemEndTime": 2530,
                        "PronAccuracy": 98.37366,
                        "DetectedStress": false,
                        "Phone": "th",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 2530,
                        "MemEndTime": 2630,
                        "PronAccuracy": 99.75654,
                        "DetectedStress": false,
                        "Phone": "ae",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 2630,
                        "MemEndTime": 2730,
                        "PronAccuracy": 99.75149,
                        "DetectedStress": false,
                        "Phone": "ng",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 2730,
                        "MemEndTime": 2830,
                        "PronAccuracy": 99.767265,
                        "DetectedStress": false,
                        "Phone": "k",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 2830,
                        "MemEndTime": 2910,
                        "PronAccuracy": 99.72817,
                        "DetectedStress": false,
                        "Phone": "y",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 2910,
                        "MemEndTime": 3170,
                        "PronAccuracy": 99.7612,
                        "DetectedStress": false,
                        "Phone": "uw",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    }
                ]
            }
        ],
        "SessionId": "E6B94BA9-6***-B***-8***-9C4B****5176",
        "AudioUrl": "",
        "SentenceInfoSet": [
            {
                "SuggestedScore": 0,
                "PronAccuracy": 99.52305,
                "PronFluency": 0.93664527,
                "PronCompletion": 1,
                "KeyWordHits": [
                    0.0
                ],
                "Words": [
                    {
                        "KeywordTag": 0,
                        "MemBeginTime": 2330,
                        "MemEndTime": 3170,
                        "PronAccuracy": 99.52305,
                        "PronFluency": 0.93664527,
                        "ReferenceWord": "",
                        "Word": "thankyou",
                        "MatchTag": 0,
                        "PhoneInfos": [
                            {
                                "MemBeginTime": 2330,
                                "MemEndTime": 2530,
                                "PronAccuracy": 98.37366,
                                "DetectedStress": false,
                                "Phone": "th",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 2530,
                                "MemEndTime": 2630,
                                "PronAccuracy": 99.75654,
                                "DetectedStress": false,
                                "Phone": "ae",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 2630,
                                "MemEndTime": 2730,
                                "PronAccuracy": 99.75149,
                                "DetectedStress": false,
                                "Phone": "ng",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 2730,
                                "MemEndTime": 2830,
                                "PronAccuracy": 99.767265,
                                "DetectedStress": false,
                                "Phone": "k",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 2830,
                                "MemEndTime": 2910,
                                "PronAccuracy": 99.72817,
                                "DetectedStress": false,
                                "Phone": "y",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 2910,
                                "MemEndTime": 3170,
                                "PronAccuracy": 99.7612,
                                "DetectedStress": false,
                                "Phone": "uw",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            }
                        ]
                    }
                ],
                "SentenceId": -1,
                "RefTextId": 0,
                "UnKeyWordHits": [
                    0.0
                ]
            }
        ],
        "Status": "Evaluating"
    }
}
```

