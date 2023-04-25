**Example 1: 菲律宾SSSID/UMID识别**

菲律宾SSSID/UMID识别

Input: 

```
tccli ocr RecognizePhilippinesSssIDOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --ReturnHeadImage false
```

Output: 
```
{
    "Response": {
        "Birthday": {
            "Polygon": [
                {
                    "X": 543,
                    "Y": 805
                },
                {
                    "X": 754,
                    "Y": 805
                },
                {
                    "X": 754,
                    "Y": 842
                },
                {
                    "X": 543,
                    "Y": 842
                }
            ],
            "Value": "JULY 7,1980"
        },
        "FullName": {
            "Polygon": [
                {
                    "X": 540,
                    "Y": 609
                },
                {
                    "X": 1094,
                    "Y": 609
                },
                {
                    "X": 1094,
                    "Y": 664
                },
                {
                    "X": 540,
                    "Y": 664
                }
            ],
            "Value": "JEFFREY"
        },
        "HeadPortrait": {
            "Polygon": [],
            "Value": ""
        },
        "LicenseNumber": {
            "Polygon": [
                {
                    "X": 533,
                    "Y": 736
                },
                {
                    "X": 1014,
                    "Y": 739
                },
                {
                    "X": 1014,
                    "Y": 816
                },
                {
                    "X": 533,
                    "Y": 813
                }
            ],
            "Value": "33-111111-1"
        },
        "RequestId": "11111-11111-11111-11111"
    }
}
```

