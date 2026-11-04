**Example 1: 成功示例**



Input: 

```
tccli ocr GenerateTextEmbedding --cli-unfold-argument  \
    --Model 1 \
    --Inputs 文本向量是什么？ \
    --TextType query \
    --Instruction Represent the query
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Embedding": [
                    -5.9178405e-05
                ],
                "Index": 0
            }
        ],
        "InputTokens": 36,
        "TotalTokens": 36,
        "RequestId": "58ed3cc0-4977-48f3-8cb8-b241bd7e50e2"
    }
}
```

