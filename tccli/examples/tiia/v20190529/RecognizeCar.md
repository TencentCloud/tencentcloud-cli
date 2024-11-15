**Example 1: 车辆识别示例代码**



Input: 

```
tccli tiia RecognizeCar --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "CarCoords": [
            {
                "X": 513,
                "Y": 651
            },
            {
                "X": 513,
                "Y": 441
            },
            {
                "X": 780,
                "Y": 441
            },
            {
                "X": 780,
                "Y": 651
            }
        ],
        "CarTags": [
            {
                "Serial": "途安",
                "Brand": "大众",
                "Type": "MPV",
                "Color": "白",
                "Confidence": 93,
                "Year": 2008,
                "CarLocation": [
                    {
                        "X": 513,
                        "Y": 651
                    },
                    {
                        "X": 513,
                        "Y": 441
                    },
                    {
                        "X": 780,
                        "Y": 441
                    },
                    {
                        "X": 780,
                        "Y": 651
                    }
                ],
                "PlateContent": null,
                "PlateConfidence": null,
                "TypeConfidence": null,
                "ColorConfidence": null,
                "Orientation": null,
                "OrientationConfidence": null
            },
            {
                "Serial": "君越",
                "Brand": "别克",
                "Type": "中型车",
                "Color": "银灰",
                "Confidence": 47,
                "Year": 2009,
                "CarLocation": [
                    {
                        "X": 45,
                        "Y": 658
                    },
                    {
                        "X": 45,
                        "Y": 459
                    },
                    {
                        "X": 313,
                        "Y": 459
                    },
                    {
                        "X": 313,
                        "Y": 658
                    }
                ],
                "PlateContent": null,
                "PlateConfidence": null,
                "TypeConfidence": null,
                "ColorConfidence": null,
                "Orientation": null,
                "OrientationConfidence": null
            }
        ],
        "RequestId": "81235fb9-d91e-4a40-91ac-9ef5675954a2"
    }
}
```

