**Example 1: 关键词句子生成调用示例**

通过输入两个中文关键词生成句子。

Input: 

```
tccli nlp GenerateKeywordSentence --cli-unfold-argument  \
    --WordList 老鼠 月光 \
    --Number 2 \
    --Domain general
```

Output: 
```
{
    "Response": {
        "KeywordSentenceList": [
            {
                "TargetText": "12月下旬，老鼠渐渐苏醒，月光温柔，生肖鼠喜从天降。"
            },
            {
                "TargetText": "在这里，老鼠看到了月亮，这就是月光。"
            }
        ],
        "RequestId": "033daa29-dd1a-4f18-aa3b-b7a6b4d4dada"
    }
}
```

