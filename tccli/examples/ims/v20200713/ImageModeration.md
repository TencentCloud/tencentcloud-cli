**Example 1: 图片同步检测**

图片同步检测

Input: 

```
tccli ims ImageModeration --cli-unfold-argument  \
    --BizType test_1001 \
    --DataId 1213 \
    --FileUrl https://xxx.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7",
        "DataId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7",
        "BizType": "test_1001",
        "Suggestion": "Block",
        "Label": "Porn",
        "SubLabel": "SexyBehavior",
        "Score": 90,
        "HitFlag": 1,
        "LabelResults": [
            {
                "Scene": "Porn",
                "Suggestion": "Block",
                "Label": "Porn",
                "SubLabel": "SexyBehavior",
                "Score": 90,
                "Details": [
                    {
                        "Id": 0,
                        "Name": "SexBehavior",
                        "Score": 90
                    }
                ]
            }
        ],
        "ObjectResults": [
            {
                "Scene": "QrCode",
                "Suggestion": "Block",
                "Label": "Ad",
                "SubLabel": "",
                "Score": 100,
                "Names": [
                    "QRCODE"
                ],
                "Details": [
                    {
                        "Id": 0,
                        "Name": "QRCODE",
                        "Value": "https://test.com/test",
                        "Score": 100,
                        "Location": {
                            "X": 155.01746,
                            "Y": 396.01746,
                            "Width": 769.9824,
                            "Height": 769.98254,
                            "Rotate": 0
                        },
                        "SubLabel": "abc",
                        "GroupId": "abc",
                        "ObjectId": "abc"
                    }
                ]
            }
        ],
        "OcrResults": [
            {
                "HitFlag": 0,
                "Scene": "OCR",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Text": "hello world",
                "Details": [
                    {
                        "Text": "hello world",
                        "Label": "",
                        "LibId": "",
                        "LibName": "",
                        "Keywords": [],
                        "Rate": 0,
                        "Score": 0,
                        "Location": {
                            "X": 8,
                            "Y": 0,
                            "Width": 111,
                            "Height": 19,
                            "Rotate": 0
                        }
                    }
                ]
            }
        ],
        "LibResults": [
            {
                "Scene": "Similar",
                "Label": "Porn",
                "SubLabel": "",
                "Score": 99,
                "Details": [
                    {
                        "LibName": "123",
                        "Score": 99,
                        "Label": "Porn",
                        "Tag": "",
                        "ImageId": "111",
                        "Id": 0,
                        "LibId": ""
                    }
                ],
                "Suggestion": "Block"
            }
        ],
        "RecognitionResults": [
            {
                "Label": "Scene",
                "Tags": [
                    {
                        "Name": "MedicalImage",
                        "Score": 30,
                        "Location": {
                            "X": 0,
                            "Y": 0,
                            "Width": 0,
                            "Height": 0,
                            "Rotate": 0
                        }
                    }
                ]
            }
        ],
        "Extra": ""
    }
}
```

