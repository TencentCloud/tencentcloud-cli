**Example 1: 提交高级图像分析任务**

提交一个图片链接作为输入的图像分析接口

Input: 

```
tccli tci SubmitImageTaskPlus --cli-unfold-argument  \
    --Functions.EnableFaceIdentify true \
    --Functions.EnableFaceDetect true \
    --Functions.EnableFaceExpression true \
    --Functions.EnableGesture true \
    --Functions.EnableStudentBodyMovements true \
    --Functions.EnableLightJudge true \
    --FileType picture_url \
    --FileContent http://xxx.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "eeadcc79-13b2-4e1e-a913-d3b8a1cdaf2b",
        "JobId": 0,
        "Progress": 100,
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
                    "LightValue": 209,
                    "LightLevel": ""
                },
                "TimeInfoResult": null
            },
            {
                "FaceIdentifyResult": null,
                "FaceInfoResult": {
                    "Left": 159,
                    "Top": 115,
                    "Width": 184,
                    "Height": 184,
                    "FrameWidth": 500,
                    "FrameHeight": 500,
                    "FaceRatio": 7.31
                },
                "FacePoseResult": {
                    "Direction": "frontal",
                    "Yaw": -1.6001276,
                    "Pitch": 4.0072374,
                    "Roll": 0.96360093
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
                "TimeInfoResult": null
            }
        ]
    }
}
```

