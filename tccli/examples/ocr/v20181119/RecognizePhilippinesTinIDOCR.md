**Example 1: 菲律宾TinID识别**



Input: 

```
tccli ocr RecognizePhilippinesTinIDOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --ReturnHeadImage false
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [],
            "Value": "18 A KATIPUNAN ST."
        },
        "Birthday": {
            "Polygon": [
                {
                    "X": 665,
                    "Y": 737
                },
                {
                    "X": 997,
                    "Y": 737
                },
                {
                    "X": 997,
                    "Y": 787
                },
                {
                    "X": 665,
                    "Y": 787
                }
            ],
            "Value": "August 17,1902"
        },
        "FullName": {
            "Polygon": [],
            "Value": "VERGARA,AMALIA ALBIOR"
        },
        "HeadPortrait": {
            "Polygon": [],
            "Value": ""
        },
        "IssueDate": {
            "Polygon": [
                {
                    "X": 665,
                    "Y": 737
                },
                {
                    "X": 997,
                    "Y": 737
                },
                {
                    "X": 997,
                    "Y": 787
                },
                {
                    "X": 665,
                    "Y": 787
                }
            ],
            "Value": "August 17,1902"
        },
        "LicenseNumber": {
            "Polygon": [
                {
                    "X": 505,
                    "Y": 522
                },
                {
                    "X": 897,
                    "Y": 522
                },
                {
                    "X": 897,
                    "Y": 572
                },
                {
                    "X": 505,
                    "Y": 572
                }
            ],
            "Value": "497-881-123-123"
        },
        "RequestId": "11111-11111-11111-11111"
    }
}
```

