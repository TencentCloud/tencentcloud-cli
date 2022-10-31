**Example 1: 发音数据传输接口附带初始化过程（常用实践）——英语句子**

句子评测模式（Evalmode为1，英语）：对句子“thank you”进行评测

Input: 

```
tccli soe TransmitOralProcessWithInit --cli-unfold-argument  \
    --ScoreCoeff 1.0 \
    --VoiceEncodeType 1 \
    --UserVoiceData VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5 \
    --IsEnd 0 \
    --ServerType 0 \
    --VoiceFileType 1 \
    --SessionId stress_test_956938 \
    --SeqId 1 \
    --RefText thankyou \
    --WorkMode 0 \
    --EvalMode 1
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

**Example 2: 发音数据传输接口附带初始化过程（常用实践）——中文汉字**

单字评测模式（Evalmode为0，中文）：对汉字“叫”进行评测

Input: 

```
tccli soe TransmitOralProcessWithInit --cli-unfold-argument  \
    --ScoreCoeff 1.0 \
    --VoiceEncodeType 1 \
    --UserVoiceData VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5 \
    --IsEnd 0 \
    --ServerType 1 \
    --VoiceFileType 1 \
    --SessionId stress_test_956938 \
    --SeqId 1 \
    --RefText 叫 \
    --WorkMode 0 \
    --EvalMode 0
```

Output: 
```
{
    "Response": {
        "SuggestedScore": 52.00305,
        "PronAccuracy": 52.00305,
        "PronFluency": 0.89224815,
        "PronCompletion": 1,
        "RequestId": "59a97be8-4***-4***-b***-8458*****826",
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
                "MemBeginTime": 1060,
                "MemEndTime": 1980,
                "PronAccuracy": 52.00305,
                "PronFluency": 0.89224815,
                "ReferenceWord": "",
                "Word": "叫",
                "MatchTag": 0,
                "PhoneInfos": [
                    {
                        "MemBeginTime": 1060,
                        "MemEndTime": 1310,
                        "PronAccuracy": 61.52326,
                        "DetectedStress": false,
                        "Phone": "j",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 1310,
                        "MemEndTime": 1600,
                        "PronAccuracy": 0.15919228,
                        "DetectedStress": false,
                        "Phone": "i4",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    },
                    {
                        "MemBeginTime": 1600,
                        "MemEndTime": 1980,
                        "PronAccuracy": 73.16487,
                        "DetectedStress": false,
                        "Phone": "ao",
                        "ReferencePhone": "",
                        "ReferenceLetter": "",
                        "Stress": false,
                        "MatchTag": 0
                    }
                ]
            }
        ],
        "SessionId": "B3617A2B-3***-4***-B***-7DB*****49B7",
        "AudioUrl": "https://soe-125*****09.cos.ap-****.myqcloud.com/125*****49/default/20210527/audio/3a0a7c84-c***-4***-a***-a15ea9775a68.mp3",
        "SentenceInfoSet": [
            {
                "SuggestedScore": 0,
                "PronAccuracy": 52.00305,
                "PronFluency": 0.89224815,
                "PronCompletion": 1,
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
                        "MemBeginTime": 1060,
                        "MemEndTime": 1980,
                        "PronAccuracy": 52.00305,
                        "PronFluency": 0.89224815,
                        "ReferenceWord": "",
                        "Word": "叫",
                        "MatchTag": 0,
                        "PhoneInfos": [
                            {
                                "MemBeginTime": 1060,
                                "MemEndTime": 1310,
                                "PronAccuracy": 61.52326,
                                "DetectedStress": false,
                                "Phone": "j",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 1310,
                                "MemEndTime": 1600,
                                "PronAccuracy": 0.15919228,
                                "DetectedStress": false,
                                "Phone": "i4",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            },
                            {
                                "MemBeginTime": 1600,
                                "MemEndTime": 1980,
                                "PronAccuracy": 73.16487,
                                "DetectedStress": false,
                                "Phone": "ao",
                                "ReferencePhone": "",
                                "ReferenceLetter": "",
                                "Stress": false,
                                "MatchTag": 0
                            }
                        ]
                    }
                ],
                "SentenceId": -1
            }
        ],
        "Status": "Finished"
    }
}
```

