**Example 1: 发起图片审核任务**

使用模板 ID 10 发起图片审核任务。

Input: 

```
tccli vod ReviewImage --cli-unfold-argument  \
    --Definition 10 \
    --FileId 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "MediaReviewResult": {
            "Suggestion": "block",
            "Label": "Porn",
            "Form": "Image",
            "SegmentSet": [
                {
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Label": "Porn",
                    "SubLabel": "SexyBehavior",
                    "Form": "Image",
                    "AreaCoordSet": [],
                    "Text": "",
                    "KeywordSet": []
                }
            ],
            "SegmentSetFileUrl": "xxx/a.mp4",
            "SegmentSetFileUrlExpireTime": "2020-09-07T00:00:00+08:00"
        },
        "ReviewResultSet": [
            {
                "Type": "Porn.Image",
                "PornImageResult": {
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Label": "porn"
                },
                "TerrorismImageResult": null,
                "PoliticalImageResult": null,
                "PornOcrResult": null,
                "TerrorismOcrResult": null,
                "PoliticalOcrResult": null
            }
        ]
    }
}
```

