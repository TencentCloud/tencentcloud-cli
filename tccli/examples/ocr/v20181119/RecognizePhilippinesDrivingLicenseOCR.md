**Example 1: 菲律宾驾驶证识别示例**



Input: 

```
tccli ocr RecognizePhilippinesDrivingLicenseOCR --cli-unfold-argument  \
    --ReturnHeadImage true \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [
                {
                    "X": "442",
                    "Y": "489"
                },
                {
                    "X": "529",
                    "Y": "489"
                },
                {
                    "X": "529",
                    "Y": "506"
                },
                {
                    "X": "442",
                    "Y": "506"
                }
            ],
            "Value": "28 PAYAPA ST BAGONG DIWA"
        },
        "AgencyCode": {
            "Polygon": [],
            "Value": ""
        },
        "Birthday": {
            "Polygon": [],
            "Value": ""
        },
        "ExpiresDate": {
            "Polygon": [],
            "Value": ""
        },
        "FirstName": {
            "Polygon": [],
            "Value": ""
        },
        "HeadPortrait": {
            "Polygon": [],
            "Value": ""
        },
        "LastName": {
            "Polygon": [],
            "Value": ""
        },
        "LicenseNo": {
            "Polygon": [],
            "Value": ""
        },
        "MiddleName": {
            "Polygon": [],
            "Value": ""
        },
        "Name": {
            "Polygon": [],
            "Value": ",  "
        },
        "Nationality": {
            "Polygon": [],
            "Value": ""
        },
        "RequestId": "1234-1234-1234-1234",
        "Sex": {
            "Polygon": [],
            "Value": ""
        }
    }
}
```

