**Example 1: RecognizePhilippinesSssIDOCR调用**



Input: 

```
tccli ocr RecognizePhilippinesSssIDOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
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
                    "X": 82,
                    "Y": 55
                },
                {
                    "X": 195,
                    "Y": 55
                },
                {
                    "X": 195,
                    "Y": 67
                },
                {
                    "X": 82,
                    "Y": 67
                }
            ],
            "Value": "PAMELAL OCAMPO"
        },
        "HeadPortrait": {
            "Polygon": [],
            "Value": ""
        },
        "LicenseNumber": {
            "Polygon": [
                {
                    "X": 82,
                    "Y": 85
                },
                {
                    "X": 187,
                    "Y": 85
                },
                {
                    "X": 187,
                    "Y": 99
                },
                {
                    "X": 82,
                    "Y": 99
                }
            ],
            "Value": "04-0751449-0"
        },
        "RequestId": "0e20a043-d3da-40e8-b576-59e33fff3b55"
    }
}
```

