**Example 1: 人脸检测与属性分析**



Input: 

```
tccli iai DetectFaceAttributes --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --FaceAttributesType eye
```

Output: 
```
{
    "Response": {
        "ImageWidth": 550,
        "ImageHeight": 366,
        "FaceModelVersion": "3.0",
        "FaceDetailInfos": [
            {
                "FaceRect": {
                    "X": 375,
                    "Y": 37,
                    "Width": 63,
                    "Height": 82
                },
                "FaceDetailAttributesInfo": {
                    "Age": 0,
                    "Beauty": 0,
                    "Emotion": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Eye": {
                        "Glass": {
                            "Type": 0,
                            "Probability": 0.99936753511429
                        },
                        "EyeOpen": {
                            "Type": 0,
                            "Probability": 0.99949336051941
                        },
                        "EyelidType": {
                            "Type": 1,
                            "Probability": 0.75467920303345
                        },
                        "EyeSize": {
                            "Type": 2,
                            "Probability": 0.59152442216873
                        }
                    },
                    "Eyebrow": {
                        "EyebrowDensity": {
                            "Type": 0,
                            "Probability": 0
                        },
                        "EyebrowCurve": {
                            "Type": 0,
                            "Probability": 0
                        },
                        "EyebrowLength": {
                            "Type": 0,
                            "Probability": 0
                        }
                    },
                    "Gender": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Hair": {
                        "Length": {
                            "Type": 0,
                            "Probability": 0
                        },
                        "Bang": {
                            "Type": 0,
                            "Probability": 0
                        },
                        "Color": {
                            "Type": 0,
                            "Probability": 0
                        }
                    },
                    "Hat": {
                        "Style": {
                            "Type": 0,
                            "Probability": 0
                        },
                        "Color": {
                            "Type": 0,
                            "Probability": 0
                        }
                    },
                    "HeadPose": {
                        "Pitch": 0,
                        "Yaw": 0,
                        "Roll": 0
                    },
                    "Mask": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Mouth": {
                        "MouthOpen": {
                            "Type": 0,
                            "Probability": 0
                        }
                    },
                    "Moustache": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Nose": {
                        "Type": 2,
                        "Probability": 0.75233882665634
                    },
                    "Shape": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Skin": {
                        "Type": 0,
                        "Probability": 0
                    },
                    "Smile": 0
                }
            }
        ],
        "RequestId": "b2c154b9-4620-4d37-8fd1-f6af3748f998"
    }
}
```

