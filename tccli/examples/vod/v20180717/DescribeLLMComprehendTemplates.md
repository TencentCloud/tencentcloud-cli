**Example 1: 获取现有模板列表**



Input: 

```
tccli vod DescribeLLMComprehendTemplates --cli-unfold-argument  \
    --SubAppId 200000
```

Output: 
```
{
    "Response": {
        "LLMComprehendTemplateSet": [
            {
                "Asr": {
                    "Switch": "ON"
                },
                "Comment": "适用于解析讲座、会议录制等不依赖画面视觉的内容",
                "CreateTime": "2026-02-05T12:00:00+08:00",
                "Definition": 100,
                "FaceRecognition": {
                    "DefaultLibraryLabelSet": [],
                    "FaceLibrary": "",
                    "Score": 0.95,
                    "Switch": "OFF",
                    "UserDefineLibraryLabelSet": []
                },
                "Level": "Audio",
                "Name": "基础音频解析模版",
                "Summary": {
                    "ExtendedParameter": "",
                    "Switch": "ON"
                },
                "Type": "Preset",
                "UpdateTime": "2026-01-29T12:00:00+08:00"
            }
        ],
        "TotalCount": 5,
        "RequestId": "3a320b20-67e3-4946-a482-f94a5e6ae435"
    }
}
```

