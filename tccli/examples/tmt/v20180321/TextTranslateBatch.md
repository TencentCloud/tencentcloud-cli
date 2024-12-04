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
        ],
        "UsedAmount": 9
    }
}
```

**Example 2: 批量文本翻译示例**

带术语库例句库

Input: 

```
tccli tmt TextTranslateBatch --cli-unfold-argument  \
    --Source auto \
    --Target en \
    --ProjectId 0 \
    --SourceTextList 你好啊 这是你的苹果 \
    --TermRepoIDList 753899732b0611efbb47037fdf41da5a \
    --SentRepoIDList 
```

Output: 
```
{
    "Response": {
        "RequestId": "abf2a2a1-a0da-4d7d-b539-cc34322b78a4",
        "Source": "zh",
        "Target": "en",
        "TargetTextList": [
            "What's up man!",
            "This is your apple"
        ],
        "UsedAmount": 9
    }
}
```

