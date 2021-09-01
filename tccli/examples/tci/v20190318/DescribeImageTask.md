**Example 1: 拉取任务详情**

拉取任务详情

Input: 

```
tccli tci DescribeImageTask --cli-unfold-argument  \
    --JobId task_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ff1e1455-b2a9-4cdb-9387-30989c993c03",
        "JobId": 222,
        "Progress": 100,
        "TotalCount": 10,
        "ResultSet": [
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 131,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 104400,
                    "EndTs": 104400,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 130,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 202500,
                    "EndTs": 202500,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 130,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 298800,
                    "EndTs": 298800,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 130,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 396000,
                    "EndTs": 396000,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 127,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 495000,
                    "EndTs": 495000,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": {
                    "Left": 1138,
                    "Top": 388,
                    "Width": 156,
                    "Height": 156,
                    "FrameWidth": 1080,
                    "FrameHeight": 1920,
                    "FaceRatio": 21.293596
                },
                "FacePoseResult": {
                    "Direction": "frontal",
                    "Yaw": 7.2338576,
                    "Pitch": -0.60113126,
                    "Roll": 4.263466
                },
                "FaceAttrResult": {
                    "Sex": "male",
                    "Age": 24
                },
                "FaceExpressionResult": {
                    "Expression": "neutral",
                    "Confidence": 55
                },
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": null,
                "TimeInfoResult": {
                    "StartTs": 591300,
                    "EndTs": 591300,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 124,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 591300,
                    "EndTs": 591300,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": {
                    "Left": 799,
                    "Top": 410,
                    "Width": 117,
                    "Height": 117,
                    "FrameWidth": 1080,
                    "FrameHeight": 1920,
                    "FaceRatio": 15.798129
                },
                "FacePoseResult": {
                    "Direction": "frontal",
                    "Yaw": 14.297856,
                    "Pitch": 1.3801595,
                    "Roll": -2.8457966
                },
                "FaceAttrResult": {
                    "Sex": "male",
                    "Age": 28
                },
                "FaceExpressionResult": {
                    "Expression": "neutral",
                    "Confidence": 99
                },
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": null,
                "TimeInfoResult": {
                    "StartTs": 687600,
                    "EndTs": 687600,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": null,
                "FacePoseResult": null,
                "FaceAttrResult": null,
                "FaceExpressionResult": null,
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": {
                    "LightValue": 127,
                    "LightLevel": ""
                },
                "TimeInfoResult": {
                    "StartTs": 687600,
                    "EndTs": 687600,
                    "Duration": 0
                }
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": {
                    "Left": 875,
                    "Top": 417,
                    "Width": 209,
                    "Height": 209,
                    "FrameWidth": 1080,
                    "FrameHeight": 1920,
                    "FaceRatio": 17.596209
                },
                "FacePoseResult": {
                    "Direction": "frontal",
                    "Yaw": 12.399566,
                    "Pitch": 2.138196,
                    "Roll": 1.1387303
                },
                "FaceAttrResult": {
                    "Sex": "male",
                    "Age": 26
                },
                "FaceExpressionResult": {
                    "Expression": "neutral",
                    "Confidence": 99
                },
                "HandTrackingResult": null,
                "GestureResult": null,
                "TeacherBodyMovementResult": null,
                "StudentBodyMovementResult": null,
                "LightResult": null,
                "TimeInfoResult": {
                    "StartTs": 785700,
                    "EndTs": 785700,
                    "Duration": 0
                }
            }
        ]
    }
}
```

