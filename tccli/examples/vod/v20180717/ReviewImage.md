**Example 1: 发起图片智能识别任务**



Input: 

```
tccli vod ReviewImage --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "ReviewResultSet": [
            {
                "Type": "Porn.Image",
                "PornImageResult": {
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Label": "sexy"
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

