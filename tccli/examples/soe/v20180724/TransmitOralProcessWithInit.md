**Example 1: 传输语音进行发音评估附带初始化过程（常用实践）**

传输语音进行发音评估附带初始化过程（常用实践）——句子模式（Evalmode为1）

Input: 

```
tccli soe TransmitOralProcessWithInit --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --VoiceFileType 1 \
    --SeqId 1 \
    --VoiceEncodeType 1 \
    --IsEnd 0 \
    --UserVoiceData VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5 \
    --WorkMode 0 \
    --RefText again \
    --EvalMode 0 \
    --ScoreCoeff 3.5
```

Output: 
```
{
    "Response": {
        "SuggestedScore": 99.52305,
        "PronAccuracy": 99.52305,
        "PronFluency": 0.93664527,
        "PronCompletion": 1,
        "RequestId": "1067cb5d-da3f-4205-b1c6-6b4632672a0e",
        "Words": [
            {
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
                        "Stress": false,
                        "MatchTag": 0
                    }
                ]
            }
        ],
        "SessionId": "E6B94BA9-48C7-4DCF-8BDD-9C4B83205176",
        "AudioUrl": "",
        "SentenceInfoSet": [
            {
                "SuggestedScore": 0,
                "PronAccuracy": 99.52305,
                "PronFluency": 0.93664527,
                "PronCompletion": 1,
                "Words": [
                    {
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
                                "Stress": false,
                                "MatchTag": 0
                            }
                        ]
                    }
                ],
                "SentenceId": -1
            }
        ],
        "Status": "Evaluating"
    }
}
```

