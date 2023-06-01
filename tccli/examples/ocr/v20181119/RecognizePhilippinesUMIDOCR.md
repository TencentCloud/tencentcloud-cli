**Example 1: 菲律宾UMID识别**

菲律宾UMID识别

Input: 

```
tccli ocr RecognizePhilippinesUMIDOCR --cli-unfold-argument  \
    --ImageBase64 abc \
    --ImageUrl abc \
    --ReturnHeadImage True
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [
                {
                    "X": 29,
                    "Y": 98
                },
                {
                    "X": 67,
                    "Y": 98
                },
                {
                    "X": 67,
                    "Y": 103
                },
                {
                    "X": 24,
                    "Y": 102
                }
            ],
            "Value": "19 MOLAVE ST. ROSA-ROSARIOH PHL 4023"
        },
        "Birthday": {
            "Polygon": [
                {
                    "X": 41,
                    "Y": 14
                },
                {
                    "X": 91,
                    "Y": 14
                },
                {
                    "X": 52,
                    "Y": 98
                },
                {
                    "X": 41,
                    "Y": 98
                }
            ],
            "Value": "1996/06/20"
        },
        "CRN": {
            "Polygon": [
                {
                    "X": 449,
                    "Y": 73
                },
                {
                    "X": 653,
                    "Y": 73
                },
                {
                    "X": 65,
                    "Y": 754
                },
                {
                    "X": 44,
                    "Y": 754
                }
            ],
            "Value": "CRN-8884732-0"
        },
        "GivenName": {
            "Polygon": [
                {
                    "X": 26,
                    "Y": 81
                },
                {
                    "X": 41,
                    "Y": 83
                },
                {
                    "X": 41,
                    "Y": 84
                },
                {
                    "X": 26,
                    "Y": 83
                }
            ],
            "Value": "ARMAINE"
        },
        "HeadPortrait": {
            "Polygon": [
                {
                    "X": 16,
                    "Y": 73
                },
                {
                    "X": 23,
                    "Y": 73
                },
                {
                    "X": 23,
                    "Y": 10
                },
                {
                    "X": 1,
                    "Y": 10
                }
            ],
            "Value": "/9j/4AAQSkZp6nI6XG5Dg+oFVdzf32/76oorpSV2Zn//2Q=="
        },
        "MiddleName": {
            "Polygon": [
                {
                    "X": 29,
                    "Y": 89
                },
                {
                    "X": 39,
                    "Y": 89
                },
                {
                    "X": 39,
                    "Y": 91
                },
                {
                    "X": 29,
                    "Y": 91
                }
            ],
            "Value": "IEGA"
        },
        "RequestId": "6790280d-02e8-4bf2-8aa6-9e95c1a5ef97",
        "Sex": {
            "Polygon": [
                {
                    "X": 35,
                    "Y": 95
                },
                {
                    "X": 42,
                    "Y": 15
                },
                {
                    "X": 342,
                    "Y": 96
                },
                {
                    "X": 25,
                    "Y": 96
                }
            ],
            "Value": "F"
        },
        "Surname": {
            "Polygon": [
                {
                    "X": 25,
                    "Y": 74
                },
                {
                    "X": 44,
                    "Y": 74
                },
                {
                    "X": 44,
                    "Y": 84
                },
                {
                    "X": 25,
                    "Y": 84
                }
            ],
            "Value": "SINO"
        }
    }
}
```

