**Example 1: 图片同步检测**

图片同步检测

Input: 

```
tccli ims ImageModeration --cli-unfold-argument  \
    --BizType 182600012300002017 \
    --DataId a61237dd-c2a0-43e7-a3da-d27022d39ba7 \
    --FileUrl https://cmstest-123.cos.ap-guangzhou.myqcloud.com/image.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7",
        "DataId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7",
        "BizType": "182600012300002017",
        "Suggestion": "Block",
        "FileMD5": "",
        "Label": "Porn",
        "SubLabel": "SexyBehavior",
        "Score": 90,
        "LabelResults": [
            {
                "Scene": "Porn",
                "Suggestion": "Block",
                "Label": "Porn",
                "SubLabel": "SexyBehavior",
                "Score": 90,
                "Details": []
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
                        "ObjectId": "",
                        "SubLabel": "QRCODE",
                        "Score": 100,
                        "Location": {
                            "X": 155.01746,
                            "Y": 396.01746,
                            "Width": 769.9824,
                            "Height": 769.98254,
                            "Rotate": 0
                        }
                    }
                ]
            }
        ],
        "OcrResults": [],
        "LibResults": [],
        "RecognitionResults": [],
        "Extra": ""
    }
}
```

