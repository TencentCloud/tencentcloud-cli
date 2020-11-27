**Example 1: 人脸检测与分析接口**



Input: 

```
tccli iai DetectFace --cli-unfold-argument  \
    --MaxFaceNum 1 \
    --MinFaceSize 40 \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --NeedFaceAttributes 0 \
    --NeedQualityDetection 0
```

Output: 
```
{
    "Response": {
        "ImageWidth": 640,
        "ImageHeight": 440,
        "FaceInfos": [
            {
                "X": 156,
                "Y": 129,
                "Width": 196,
                "Height": 196,
                "FaceAttributesInfo": {
                    "Gender": 0,
                    "Age": 0,
                    "Expression": 0,
                    "Hat": false,
                    "Glass": false,
                    "EyeOpen": true,
                    "Mask": false,
                    "Hair": {
                        "Length": 0,
                        "Bang": 0,
                        "Color": 0
                    },
                    "Pitch": 0,
                    "Yaw": 0,
                    "Roll": 0,
                    "Beauty": 0
                },
                "FaceQualityInfo": {
                    "Score": 0,
                    "Sharpness": 0,
                    "Brightness": 0,
                    "Completeness": {
                        "Eyebrow": 0,
                        "Eye": 0,
                        "Nose": 0,
                        "Cheek": 0,
                        "Mouth": 0,
                        "Chin": 0
                    }
                }
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "a574102d-1b86-48a7-a08b-6a741a8fedb6"
    }
}
```

**Example 2: 人脸检测与分析接口-2**



Input: 

```
tccli iai DetectFace --cli-unfold-argument  \
    --MaxFaceNum 1 \
    --MinFaceSize 40 \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --NeedFaceAttributes 1 \
    --NeedQualityDetection 1
```

Output: 
```
{
    "Response": {
        "ImageWidth": 640,
        "ImageHeight": 440,
        "FaceInfos": [
            {
                "X": 156,
                "Y": 129,
                "Width": 196,
                "Height": 196,
                "FaceAttributesInfo": {
                    "Gender": 99,
                    "Age": 51,
                    "Expression": 99,
                    "Hat": false,
                    "Glass": false,
                    "EyeOpen": true,
                    "Mask": true,
                    "Hair": {
                        "Length": 1,
                        "Bang": 1,
                        "Color": 0
                    },
                    "Pitch": 17,
                    "Yaw": 5,
                    "Roll": -2,
                    "Beauty": 71
                },
                "FaceQualityInfo": {
                    "Score": 63,
                    "Sharpness": 73,
                    "Brightness": 47,
                    "Completeness": {
                        "Eyebrow": 99,
                        "Eye": 99,
                        "Nose": 99,
                        "Cheek": 52,
                        "Mouth": 99,
                        "Chin": 47
                    }
                }
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "bcde47b5-e6d8-446e-a538-bcecffbe306a"
    }
}
```

