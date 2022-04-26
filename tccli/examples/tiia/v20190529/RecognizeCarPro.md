**Example 1: 车辆识别示例代码**



Input: 

```
tccli tiia RecognizeCarPro --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "CarTags": [
            {
                "PlateContent": {
                    "Color": "蓝色",
                    "PlateLocation": [
                        {
                            "Y": 727,
                            "X": 508
                        },
                        {
                            "Y": 634,
                            "X": 508
                        },
                        {
                            "Y": 634,
                            "X": 777
                        },
                        {
                            "X": 777,
                            "Y": 727
                        }
                    ],
                    "Plate": "粤BT****",
                    "Type": "普通蓝牌"
                },
                "Serial": "飞驰",
                "Brand": "宾利",
                "Type": "轿车",
                "Color": "黑",
                "Confidence": 99,
                "Year": 0,
                "CarLocation": [
                    {
                        "X": 135,
                        "Y": 826
                    },
                    {
                        "Y": 191,
                        "X": 135
                    },
                    {
                        "Y": 191,
                        "X": 1116
                    },
                    {
                        "X": 1116,
                        "Y": 826
                    }
                ]
            },
            {
                "CarLocation": [
                    {
                        "X": 0,
                        "Y": 488
                    },
                    {
                        "X": 0,
                        "Y": 368
                    },
                    {
                        "X": 125,
                        "Y": 368
                    },
                    {
                        "X": 125,
                        "Y": 488
                    }
                ],
                "PlateContent": {
                    "PlateLocation": [],
                    "Plate": "",
                    "Type": "",
                    "Color": ""
                },
                "Serial": "五菱之光",
                "Brand": "东风",
                "Type": "面包车",
                "Color": "黄",
                "Confidence": 0,
                "Year": 0
            }
        ],
        "RequestId": "dabc3980-1f8d-4e8a-a943-4412d82e5df9",
        "CarCoords": [
            {
                "X": 135,
                "Y": 826
            },
            {
                "X": 135,
                "Y": 191
            },
            {
                "X": 1116,
                "Y": 191
            },
            {
                "X": 1116,
                "Y": 826
            }
        ]
    }
}
```

**Example 2: 调用失败示例**



Input: 

```
tccli tiia RecognizeCarPro --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "ad418ac5-fbfd-4bd7-8f4a-35ab085e27dd"
    }
}
```

