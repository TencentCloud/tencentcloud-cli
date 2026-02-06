**Example 1: 搜索**



Input: 

```
tccli vod SearchMediaBySemantics --cli-unfold-argument  \
    --SubAppId 1500035838 \
    --Text 包含夕阳的海边视频
```

Output: 
```
{
    "Response": {
        "RequestId": "1e7aa7b9-0f92-4fbb-9ca2-6aebdfb31543",
        "SearchResults": [
            {
                "EndTimeOffset": 159.07,
                "FileId": "966263618841114024",
                "Score": 0.58276,
                "StartTimeOffset": 109.908
            },
            {
                "EndTimeOffset": 109.708,
                "FileId": "966263618841114024",
                "Score": 0.58201,
                "StartTimeOffset": 83.141
            },
            {
                "EndTimeOffset": 82.741,
                "FileId": "966263618841114024",
                "Score": 0.46496,
                "StartTimeOffset": 10.222
            }
        ]
    }
}
```

