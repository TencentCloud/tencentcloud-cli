**Example 1: 图片同步检测**

图片同步检测

Input: 

```
tccli ims ImageModeration --cli-unfold-argument  \
    --BizType TencentCloudDefault \
    --DataId a61237dd-c2a0-43e7-a3da-d27022d39ba7 \
    --FileUrl https://cmstest-123.cos.ap-guangzhou.myqcloud.com/image.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "d636333a-0d14-4962-8287-e6e8af0a10f2",
        "FileMD5": "4c7bbbc76bf4b317222e25067e8e9739",
        "DataId": "a61237dd-c2a0-43e7-a3da-d27022d39ba7",
        "BizType": "TencentCloudDefault",
        "Suggestion": "Review",
        "Label": "Terror",
        "SubLabel": "Knife",
        "Score": 93,
        "LabelResults": [
            {
                "Scene": "Terror",
                "Suggestion": "Review",
                "Label": "Terror",
                "SubLabel": "Knife",
                "Score": 93,
                "Details": [
                    {
                        "Id": 0,
                        "Name": "Knife",
                        "Score": 93
                    }
                ]
            },
            {
                "Scene": "Illegal",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Details": []
            },
            {
                "Scene": "Teenager",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Details": []
            },
            {
                "Scene": "Porn",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 1,
                "Details": []
            },
            {
                "Scene": "Sexy",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Details": []
            }
        ],
        "ObjectResults": [
            {
                "Scene": "PolityFace",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Names": [],
                "Details": []
            },
            {
                "Scene": "AppLogo",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Names": [],
                "Details": []
            },
            {
                "Scene": "MapRecognition",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Names": [],
                "Details": []
            }
        ],
        "OcrResults": [
            {
                "Scene": "OCR",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Text": "",
                "Details": []
            }
        ],
        "LibResults": [
            {
                "Scene": "Similar",
                "Suggestion": "Pass",
                "Label": "Normal",
                "SubLabel": "",
                "Score": 0,
                "Details": []
            }
        ],
        "RecognitionResults": [],
        "Extra": "{\"TerrorInfo\":[{\"Label\":\"Terror\"}}"
    },
    "retcode": 0,
    "retmsg": "ok"
}
```

