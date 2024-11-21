**Example 1: 菲律宾UMID识别**

菲律宾UMID识别

Input: 

```
tccli ocr RecognizePhilippinesUMIDOCR --cli-unfold-argument  \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q== \
    --ImageUrl  \
    --ReturnHeadImage True
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [
                {
                    "X": 299,
                    "Y": 948
                },
                {
                    "X": 653,
                    "Y": 948
                },
                {
                    "X": 654,
                    "Y": 1007
                },
                {
                    "X": 299,
                    "Y": 1000
                }
            ],
            "Value": "19 MOLAVE *** LAGUNA PHL ****"
        },
        "Birthday": {
            "Polygon": [
                {
                    "X": 443,
                    "Y": 915
                },
                {
                    "X": 586,
                    "Y": 917
                },
                {
                    "X": 587,
                    "Y": 938
                },
                {
                    "X": 442,
                    "Y": 937
                }
            ],
            "Value": "1996/03/26"
        },
        "CRN": {
            "Polygon": [
                {
                    "X": 446,
                    "Y": 733
                },
                {
                    "X": 649,
                    "Y": 734
                },
                {
                    "X": 649,
                    "Y": 755
                },
                {
                    "X": 446,
                    "Y": 754
                }
            ],
            "Value": "CRN-***-888***-0"
        },
        "GivenName": {
            "Polygon": [
                {
                    "X": 295,
                    "Y": 832
                },
                {
                    "X": 486,
                    "Y": 833
                },
                {
                    "X": 486,
                    "Y": 855
                },
                {
                    "X": 295,
                    "Y": 854
                }
            ],
            "Value": "ARMAI***YCE"
        },
        "HeadPortrait": {
            "Polygon": [
                {
                    "X": 16,
                    "Y": 731
                },
                {
                    "X": 233,
                    "Y": 731
                },
                {
                    "X": 233,
                    "Y": 1006
                },
                {
                    "X": 16,
                    "Y": 1006
                }
            ],
            "Value": "/9j/4AAQSkZJRg.....s97n//2Q=="
        },
        "MiddleName": {
            "Polygon": [
                {
                    "X": 296,
                    "Y": 895
                },
                {
                    "X": 400,
                    "Y": 894
                },
                {
                    "X": 401,
                    "Y": 915
                },
                {
                    "X": 296,
                    "Y": 916
                }
            ],
            "Value": "ZU**EGA"
        },
        "Sex": {
            "Polygon": [
                {
                    "X": 324,
                    "Y": 915
                },
                {
                    "X": 341,
                    "Y": 915
                },
                {
                    "X": 342,
                    "Y": 936
                },
                {
                    "X": 322,
                    "Y": 935
                }
            ],
            "Value": "F"
        },
        "Surname": {
            "Polygon": [
                {
                    "X": 292,
                    "Y": 793
                },
                {
                    "X": 415,
                    "Y": 793
                },
                {
                    "X": 415,
                    "Y": 814
                },
                {
                    "X": 292,
                    "Y": 815
                }
            ],
            "Value": "SAL**INO"
        },
        "RequestId": "61d6eff2-418e-4864-b1cf-af0b91c53efb"
    }
}
```

