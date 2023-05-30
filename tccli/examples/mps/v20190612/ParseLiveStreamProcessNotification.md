**Example 1: 解析直播流事件通知内容**

回调包体描述

Input: 

```
tccli mps ParseLiveStreamProcessNotification --cli-unfold-argument  \
    --Content {"NotificationType":"AiReviewResult",XXX
```

Output: 
```
{
    "Response": {
        "NotificationType": "AiReviewResult",
        "TaskId": "2459149217-procedure-live-xxx51da009t0",
        "ProcessEofInfo": null,
        "AiReviewResultInfo": {
            "ResultSet": [
                {
                    "Type": "VoicePorn",
                    "ImagePornResultSet": [],
                    "ImageTerrorismResultSet": [],
                    "ImagePoliticalResultSet": [],
                    "VoicePornResultSet": [
                        {
                            "StartPtsTime": 0.266,
                            "EndPtsTime": 4.146,
                            "Confidence": 98,
                            "Suggestion": "block",
                            "Label": "sexual_moan"
                        }
                    ]
                }
            ]
        },
        "AiRecognitionResultInfo": null,
        "AiAnalysisResultInfo": null,
        "AiQualityControlResultInfo": null,
        "SessionId": "",
        "SessionContext": "",
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5"
    }
}
```

