**Example 1: text_embedding_v1 模型embedding**

用于文本的embedding

Input: 

```
tccli mps EmbeddingData --cli-unfold-argument  \
    --Model text_embedding_v1 \
    --Files.0.Type text \
    --Files.0.Data 今天天气不错 \
    --Prompt Instruct: Retrieve semantically similar text.\nQuery:
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Result": [
                    -0.0055236816
                ]
            }
        ],
        "Usage": {
            "InputTokens": 15,
            "TotalTokens": 15
        },
        "RequestId": "f4de2dd4-bac4-47d8-a983-8ee3ffb92f26"
    }
}
```

