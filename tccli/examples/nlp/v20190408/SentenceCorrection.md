**Example 1: 句子纠错调用示例**

对包含错别字的中文句子以及包含语法错误的英文句子进行纠错。

Input: 

```
tccli nlp SentenceCorrection --cli-unfold-argument  \
    --TextList 这位外国网友说：这是地球最安全的锅加，在这里，我从未感到过害啪！ 'We always rent a little cottages from a sheep farmer and now we know his family.'
```

Output: 
```
{
    "Response": {
        "CorrectionList": [
            {
                "BeginOffset": 16,
                "Confidence": 0,
                "CorrectWord": [
                    "国家"
                ],
                "CorrectionType": 0,
                "DescriptionEn": null,
                "DescriptionZh": null,
                "Len": 2,
                "Order": 1,
                "Word": "锅加"
            },
            {
                "BeginOffset": 30,
                "Confidence": 0,
                "CorrectWord": [
                    "怕"
                ],
                "CorrectionType": 0,
                "DescriptionEn": null,
                "DescriptionZh": null,
                "Len": 1,
                "Order": 1,
                "Word": "啪"
            },
            {
                "BeginOffset": 24,
                "Confidence": 0,
                "CorrectWord": [
                    "cottage"
                ],
                "CorrectionType": 0,
                "DescriptionEn": "It appears that the noun \"cottage\" doesn't agree with \"a little\".",
                "DescriptionZh": "在当前语境下，“cottages”作为名词和量词“a little”没有保持单复数一致，建议使用“cottage”以保持名词一致性。",
                "Len": 8,
                "Order": 2,
                "Word": "cottages"
            }
        ],
        "RequestId": "b183f9d5-b35a-4880-8a36-86883b9eea11"
    }
}
```

