**Example 1: 稠密关键点接口**

对请求图片进行五官定位，获得人脸的精准信息。

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
        "ImageWidth": 940,
        "ImageHeight": 930,
        "DenseFaceShapeSet": [
            {
                "X": 450,
                "Y": 230,
                "Width": 340,
                "Height": 540,
                "LeftEye": [
                    {
                        "X": 20,
                        "Y": 40
                    }
                ],
                "RightEye": [
                    {
                        "X": 80,
                        "Y": 30
                    }
                ],
                "LeftEyeBrow": [
                    {
                        "X": 94,
                        "Y": 90
                    }
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "1219c74e7-698e-4ac2-8bc4-4c996cbdda8b"
    }
}
```

