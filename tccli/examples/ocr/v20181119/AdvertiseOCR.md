**Example 1: AdvertiseOCR调用**

 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=AdvertiseOCR)

Input: 

```
tccli ocr AdvertiseOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/AdvertiseOCR/AdvertiseOCR1.jpg
```

Output: 
```
{
    "Response": {
        "ImageSize": {
            "Height": 800,
            "Width": 800
        },
        "RequestId": "72162aef-f8b6-4247-8efc-53e80311189d",
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":0}}",
                "Confidence": 100,
                "DetectedText": "永葆容颜",
                "Polygon": [
                    {
                        "X": 228,
                        "Y": 48
                    },
                    {
                        "X": 566,
                        "Y": 48
                    },
                    {
                        "X": 566,
                        "Y": 169
                    },
                    {
                        "X": 228,
                        "Y": 169
                    }
                ]
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":0}}",
                "Confidence": 100,
                "DetectedText": "CHERISH THE ACHIEVEMENTS OF LUXURY",
                "Polygon": [
                    {
                        "X": 223,
                        "Y": 166
                    },
                    {
                        "X": 569,
                        "Y": 167
                    },
                    {
                        "X": 569,
                        "Y": 194
                    },
                    {
                        "X": 223,
                        "Y": 192
                    }
                ]
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":0}}",
                "Confidence": 100,
                "DetectedText": "源于.自然的恩惠",
                "Polygon": [
                    {
                        "X": 301,
                        "Y": 219
                    },
                    {
                        "X": 494,
                        "Y": 219
                    },
                    {
                        "X": 494,
                        "Y": 246
                    },
                    {
                        "X": 301,
                        "Y": 246
                    }
                ]
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":0}}",
                "Confidence": 100,
                "DetectedText": "化妆品荣誉产品全场7折起售",
                "Polygon": [
                    {
                        "X": 232,
                        "Y": 257
                    },
                    {
                        "X": 562,
                        "Y": 257
                    },
                    {
                        "X": 562,
                        "Y": 287
                    },
                    {
                        "X": 232,
                        "Y": 287
                    }
                ]
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":0}}",
                "Confidence": 100,
                "DetectedText": "FOUDATION",
                "Polygon": [
                    {
                        "X": 407,
                        "Y": 600
                    },
                    {
                        "X": 407,
                        "Y": 766
                    },
                    {
                        "X": 383,
                        "Y": 766
                    },
                    {
                        "X": 383,
                        "Y": 600
                    }
                ]
            }
        ]
    }
}
```

