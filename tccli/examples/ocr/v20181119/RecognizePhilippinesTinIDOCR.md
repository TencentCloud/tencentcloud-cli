**Example 1: 菲律宾TinID识别调用**



Input: 

```
tccli ocr RecognizePhilippinesTinIDOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --ReturnHeadImage false
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [],
            "Value": "18 A KATIPUNAN ****** RIZAL "
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
            "Value": "August **,1972"
        },
        "FullName": {
            "Polygon": [],
            "Value": "VER******ALBIOR"
        },
        "HeadPortrait": {
            "Polygon": [
                {
                    "X": 1118,
                    "Y": 512
                },
                {
                    "X": 1368,
                    "Y": 512
                },
                {
                    "X": 1368,
                    "Y": 808
                },
                {
                    "X": 1118,
                    "Y": 808
                }
            ],
            "Value": "/9j/4AAQSkZJRg.....s97n//2Q=="
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
            "Value": "August **,1972"
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
            "Value": "497-***-***-000"
        },
        "RequestId": "df40cc1c-e074-44ab-ab39-cc2c105a5cd4"
    }
}
```

