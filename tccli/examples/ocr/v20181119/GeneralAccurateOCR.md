**Example 1: Recognizing general print (high-precision) ([debugging tool](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralAccurateOCR))**



Input: 

```
tccli ocr GeneralAccurateOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "Confetteria",
                "Confidence": 99,
                "ItemPolygon": {
                    "X": 449,
                    "Y": 211,
                    "Width": 115,
                    "Height": 37
                },
                "Polygon": [
                    {
                        "X": 449,
                        "Y": 231
                    },
                    {
                        "X": 452,
                        "Y": 211
                    },
                    {
                        "X": 563,
                        "Y": 227
                    },
                    {
                        "X": 560,
                        "Y": 247
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
            },
            {
                "DetectedText": "Raffaello",
                "Confidence": 99,
                "ItemPolygon": {
                    "X": 361,
                    "Y": 242,
                    "Width": 288,
                    "Height": 97
                },
                "Polygon": [
                    {
                        "X": 361,
                        "Y": 308
                    },
                    {
                        "X": 368,
                        "Y": 242
                    },
                    {
                        "X": 648,
                        "Y": 271
                    },
                    {
                        "X": 641,
                        "Y": 338
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
            },
            {
                "DetectedText": "费列罗臻点坊",
                "Confidence": 99,
                "ItemPolygon": {
                    "X": 394,
                    "Y": 316,
                    "Width": 200,
                    "Height": 56
                },
                "Polygon": [
                    {
                        "X": 394,
                        "Y": 349
                    },
                    {
                        "X": 398,
                        "Y": 316
                    },
                    {
                        "X": 593,
                        "Y": 337
                    },
                    {
                        "X": 589,
                        "Y": 371
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
            },
            {
                "DetectedText": "拉斐尔@脆雪柔",
                "Confidence": 98,
                "ItemPolygon": {
                    "X": 381,
                    "Y": 368,
                    "Width": 214,
                    "Height": 55
                },
                "Polygon": [
                    {
                        "X": 381,
                        "Y": 401
                    },
                    {
                        "X": 385,
                        "Y": 368
                    },
                    {
                        "X": 594,
                        "Y": 389
                    },
                    {
                        "X": 590,
                        "Y": 422
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
            }
        ],
        "Angel": 0,
        "RequestId": "d2a1c039-817d-455b-b2e2-f765a7261906"
    }
}
```

