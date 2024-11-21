**Example 1: 菲律宾驾驶证识别调用**



Input: 

```
tccli ocr RecognizePhilippinesDrivingLicenseOCR --cli-unfold-argument  \
    --ReturnHeadImage true \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [
                {
                    "X": 566,
                    "Y": 500
                },
                {
                    "X": 704,
                    "Y": 500
                },
                {
                    "X": 704,
                    "Y": 532
                },
                {
                    "X": 566,
                    "Y": 532
                }
            ],
            "Value": "132 LAKAS NG MAHIRAP***CITY"
        },
        "AgencyCode": {
            "Polygon": [
                {
                    "X": 1286,
                    "Y": 683
                },
                {
                    "X": 1385,
                    "Y": 683
                },
                {
                    "X": 1385,
                    "Y": 725
                },
                {
                    "X": 1286,
                    "Y": 725
                }
            ],
            "Value": "N2*"
        },
        "Birthday": {
            "Polygon": [
                {
                    "X": 911,
                    "Y": 432
                },
                {
                    "X": 1186,
                    "Y": 432
                },
                {
                    "X": 1186,
                    "Y": 483
                },
                {
                    "X": 911,
                    "Y": 483
                }
            ],
            "Value": "1992/**/22"
        },
        "ExpiresDate": {
            "Polygon": [
                {
                    "X": 557,
                    "Y": 675
                },
                {
                    "X": 1229,
                    "Y": 679
                },
                {
                    "X": 1228,
                    "Y": 736
                },
                {
                    "X": 556,
                    "Y": 732
                }
            ],
            "Value": "2024/**/22"
        },
        "FirstName": {
            "Polygon": [
                {
                    "X": 555,
                    "Y": 320
                },
                {
                    "X": 1286,
                    "Y": 314
                },
                {
                    "X": 1286,
                    "Y": 373
                },
                {
                    "X": 555,
                    "Y": 379
                }
            ],
            "Value": "GE**LD"
        },
        "HeadPortrait": {
            "Polygon": [
                {
                    "X": 108,
                    "Y": 282
                },
                {
                    "X": 536,
                    "Y": 282
                },
                {
                    "X": 536,
                    "Y": 770
                },
                {
                    "X": 108,
                    "Y": 770
                }
            ],
            "Value": "/9j/4AAQSkZJRg.....s97n//2Q=="
        },
        "LastName": {
            "Polygon": [
                {
                    "X": 555,
                    "Y": 320
                },
                {
                    "X": 1286,
                    "Y": 314
                },
                {
                    "X": 1286,
                    "Y": 373
                },
                {
                    "X": 555,
                    "Y": 379
                }
            ],
            "Value": "SA**N"
        },
        "LicenseNo": {
            "Polygon": [
                {
                    "X": 557,
                    "Y": 675
                },
                {
                    "X": 1229,
                    "Y": 679
                },
                {
                    "X": 1228,
                    "Y": 736
                },
                {
                    "X": 556,
                    "Y": 732
                }
            ],
            "Value": "N02-**-****44"
        },
        "MiddleName": {
            "Polygon": [
                {
                    "X": 555,
                    "Y": 320
                },
                {
                    "X": 1286,
                    "Y": 314
                },
                {
                    "X": 1286,
                    "Y": 373
                },
                {
                    "X": 555,
                    "Y": 379
                }
            ],
            "Value": "GO***LES"
        },
        "Name": {
            "Polygon": [
                {
                    "X": 555,
                    "Y": 320
                },
                {
                    "X": 1286,
                    "Y": 314
                },
                {
                    "X": 1286,
                    "Y": 373
                },
                {
                    "X": 555,
                    "Y": 379
                }
            ],
            "Value": "SA*****LES"
        },
        "Nationality": {
            "Polygon": [
                {
                    "X": 563,
                    "Y": 438
                },
                {
                    "X": 660,
                    "Y": 438
                },
                {
                    "X": 660,
                    "Y": 479
                },
                {
                    "X": 563,
                    "Y": 479
                }
            ],
            "Value": "PHL"
        },
        "RequestId": "f3f1b6d7-e2f1-48e1-a454-d2c8ba2e4fa0",
        "Sex": {
            "Polygon": [
                {
                    "X": 561,
                    "Y": 393
                },
                {
                    "X": 743,
                    "Y": 397
                },
                {
                    "X": 742,
                    "Y": 439
                },
                {
                    "X": 561,
                    "Y": 434
                }
            ],
            "Value": "M"
        }
    }
}
```

