**Example 1: 菲律宾VoteID识别示例**

菲律宾VoteID识别示例

Input: 

```
tccli ocr RecognizePhilippinesVoteIDOCR --cli-unfold-argument  \
    --ReturnHeadImage false \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": {
            "Polygon": [
                {
                    "X": "276",
                    "Y": "337"
                },
                {
                    "X": "351",
                    "Y": "337"
                },
                {
                    "X": "351",
                    "Y": "357"
                },
                {
                    "X": "276",
                    "Y": "357"
                }
            ],
            "Value": " IPIL,ZAMBOANGA CITY"
        },
        "Birthday": {
            "Polygon": [
                {
                    "X": "406",
                    "Y": "257"
                },
                {
                    "X": "552",
                    "Y": "257"
                },
                {
                    "X": "552",
                    "Y": "279"
                },
                {
                    "X": "406",
                    "Y": "279"
                }
            ],
            "Value": "March 13,1985"
        },
        "Citizenship": {
            "Polygon": [
                {
                    "X": "405",
                    "Y": "311"
                },
                {
                    "X": "492",
                    "Y": "311"
                },
                {
                    "X": "492",
                    "Y": "331"
                },
                {
                    "X": "404",
                    "Y": "331"
                }
            ],
            "Value": "Filipino"
        },
        "CivilStatus": {
            "Polygon": [
                {
                    "X": "407",
                    "Y": "285"
                },
                {
                    "X": "485",
                    "Y": "285"
                },
                {
                    "X": "485",
                    "Y": "304"
                },
                {
                    "X": "407",
                    "Y": "304"
                }
            ],
            "Value": "Single"
        },
        "FirstName": {
            "Polygon": [
                {
                    "X": "276",
                    "Y": "173"
                },
                {
                    "X": "344",
                    "Y": "173"
                },
                {
                    "X": "344",
                    "Y": "195"
                },
                {
                    "X": "276",
                    "Y": "195"
                }
            ],
            "Value": "ROYO"
        },
        "HeadPortrait": {
            "Polygon": [],
            "Value": ""
        },
        "LastName": {
            "Polygon": [
                {
                    "X": "276",
                    "Y": "214"
                },
                {
                    "X": "376",
                    "Y": "213"
                },
                {
                    "X": "376",
                    "Y": "238"
                },
                {
                    "X": "276",
                    "Y": "239"
                }
            ],
            "Value": "TUDTUD"
        },
        "PrecinctNo": {
            "Polygon": [
                {
                    "X": "459",
                    "Y": "415"
                },
                {
                    "X": "520",
                    "Y": "415"
                },
                {
                    "X": "520",
                    "Y": "434"
                },
                {
                    "X": "459",
                    "Y": "434"
                }
            ],
            "Value": "0398B"
        },
        "RequestId": "1234-1234-1234-1234",
        "VIN": {
            "Polygon": [
                {
                    "X": "253",
                    "Y": "128"
                },
                {
                    "X": "652",
                    "Y": "128"
                },
                {
                    "X": "652",
                    "Y": "153"
                },
                {
                    "X": "253",
                    "Y": "153"
                }
            ],
            "Value": "7502-0398B-G0987ANT10000"
        }
    }
}
```

