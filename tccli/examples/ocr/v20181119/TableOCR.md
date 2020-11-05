**Example 1: Recognizing form**



Input: 

```
tccli ocr TableOCR --cli-unfold-argument  \
    --ImageUrl http%3A%2F%2Fimg3.redocn.com%2Ftupian%2F20180301%2Fkongbaiqiuzhijianlibiaogesheji_9230633.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "ColTl": 2,
                "RowTl": 11,
                "ColBr": 4,
                "RowBr": 12,
                "Text": "",
                "Type": "body",
                "Confidence": 0,
                "Polygon": [
                    {
                        "X": 171,
                        "Y": 415
                    },
                    {
                        "X": 296,
                        "Y": 415
                    },
                    {
                        "X": 296,
                        "Y": 446
                    },
                    {
                        "X": 171,
                        "Y": 446
                    }
                ],
                "AdvancedInfo": "{}"
            },
            {
                "ColTl": 1,
                "RowTl": 7,
                "ColBr": 6,
                "RowBr": 8,
                "Text": "",
                "Type": "body",
                "Confidence": 0,
                "Polygon": [
                    {
                        "X": 91,
                        "Y": 251
                    },
                    {
                        "X": 401,
                        "Y": 251
                    },
                    {
                        "X": 401,
                        "Y": 276
                    },
                    {
                        "X": 91,
                        "Y": 276
                    }
                ],
                "AdvancedInfo": "{}"
            }
        ],
        "Data": "UEsDBBQAAA......",
        "RequestId": "436d209b-a3ad-4491-b3bf-185f217bf191"
    }
}
```

