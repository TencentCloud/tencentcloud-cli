**Example 1: 批量文本翻译调用示例**

批量文本翻译

Input: 

```
tccli tmt TextTranslateBatch --cli-unfold-argument  \
    --SourceTextList 你好 今天天气怎么样 \
    --Source zh \
    --Target en \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "beb15bd7-29aa-4f0f-9a80-574d6fc3733f",
        "Source": "zh",
        "Target": "en",
        "TargetTextList": [
            "Hello.",
            "What's the weather like today?"
        ]
    }
}
```

