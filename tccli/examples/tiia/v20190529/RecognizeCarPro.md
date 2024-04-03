**Example 1: 调用失败示例**

输入图片URL，未检测到车辆信息。

Input: 

```
tccli tiia RecognizeCarPro --cli-unfold-argument  \
    --ImageUrl http://www.test.com/a.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.NoObjectDetected",
            "Message": "未检测到目标。"
        },
        "RequestId": "ad418ac5-fbfd-4bd7-8f4a-35ab085e27dd"
    }
}
```

**Example 2: 车辆识别示例代码**

输入图片URL，成功检测到车辆信息。

Input: 

```
tccli tiia RecognizeCarPro --cli-unfold-argument  \
    --ImageUrl http://www.test.com/b.jpg
```

Output: 
```
{
    "Response": {
        "CarCoords": [
            {
                "X": 87,
                "Y": 291
            },
            {
                "X": 87,
                "Y": 1
            },
            {
                "X": 540,
                "Y": 1
            },
            {
                "X": 540,
                "Y": 291
            }
        ],
        "CarTags": [
            {
                "Brand": "奔驰",
                "CarLocation": [
                    {
                        "X": 87,
                        "Y": 291
                    },
                    {
                        "X": 87,
                        "Y": 1
                    },
                    {
                        "X": 540,
                        "Y": 1
                    },
                    {
                        "X": 540,
                        "Y": 291
                    }
                ],
                "Color": "绿",
                "ColorConfidence": 67,
                "Confidence": 64,
                "Orientation": "车头",
                "OrientationConfidence": 99,
                "PlateConfidence": 99,
                "PlateContent": {
                    "Color": "蓝色",
                    "Plate": "浙G29XY9",
                    "PlateAngle": 13.560508,
                    "PlateLocation": [
                        {
                            "X": 452,
                            "Y": 227
                        },
                        {
                            "X": 452,
                            "Y": 190
                        },
                        {
                            "X": 507,
                            "Y": 190
                        },
                        {
                            "X": 507,
                            "Y": 227
                        }
                    ],
                    "PlateStatus": "正常车牌",
                    "PlateStatusConfidence": 99,
                    "Type": "普通蓝牌"
                },
                "Serial": "奔驰GLC级",
                "Type": "SUV",
                "TypeConfidence": 54,
                "Year": 0
            }
        ],
        "RequestId": "2aba0901-31b9-456f-ad38-a2e7075d0965"
    }
}
```

