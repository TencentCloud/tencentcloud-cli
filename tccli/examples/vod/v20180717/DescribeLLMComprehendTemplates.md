**Example 1: 获取现有模板列表**



Input: 

```
tccli vod DescribeLLMComprehendTemplates --cli-unfold-argument  \
    --SubAppId 221086
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
                "Level": "Audio",
                "Name": "基础音频解析模版",
                "Summary": {
                    "ExtendedParameter": "",
                    "Switch": "ON"
                },
                "UpdateTime": "2026-01-29T12:00:00+08:00"
            }
        ],
        "TotalCount": 2,
        "RequestId": "df838f51-db7c-45c1-899d-6a8597d2afaa"
    }
}
```

