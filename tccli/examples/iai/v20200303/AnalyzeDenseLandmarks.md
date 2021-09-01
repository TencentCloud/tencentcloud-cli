**Example 1: 稠密关键点接口**



Input: 

```
tccli iai AnalyzeDenseLandmarks --cli-unfold-argument  \
    --Mode 0 \
    --Url http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "ImageWidth": 550,
        "ImageHeight": 366,
        "DenseFaceShapeSet": [
            {
                "Chin": [
                    {
                        "X": 376,
                        "Y": 66
                    }
                ],
                "LeftEye": [
                    {
                        "X": 384,
                        "Y": 66
                    }
                ],
                "RightEye": [
                    {
                        "X": 422,
                        "Y": 72
                    }
                ],
                "LeftEyeBrow": [
                    {
                        "X": 382,
                        "Y": 61
                    }
                ],
                "RightEyeBrow": [
                    {
                        "X": 428,
                        "Y": 68
                    }
                ],
                "Nose": [
                    {
                        "X": 398,
                        "Y": 69
                    }
                ],
                "MouthInside": [
                    {
                        "X": 386,
                        "Y": 98
                    }
                ],
                "MouthOutside": [
                    {
                        "X": 386,
                        "Y": 98
                    }
                ],
                "LeftPupil": [
                    {
                        "X": 390,
                        "Y": 65
                    }
                ],
                "RightPupil": [
                    {
                        "X": 416,
                        "Y": 70
                    }
                ],
                "LeftEyeBags": [
                    {
                        "X": 395,
                        "Y": 69
                    }
                ],
                "RightEyeBags": [
                    {
                        "X": 410,
                        "Y": 72
                    }
                ],
                "Forehead": [
                    {
                        "X": 376,
                        "Y": 65
                    }
                ],
                "CentralAxis": [
                    {
                        "X": 405,
                        "Y": 54
                    }
                ],
                "X": 375,
                "Y": 37,
                "Width": 63,
                "Height": 82
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "cebb639a-ec53-4a23-a5a5-fbcc5f0ae2bc"
    }
}
```

