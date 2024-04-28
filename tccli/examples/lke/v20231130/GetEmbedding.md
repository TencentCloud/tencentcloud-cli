**Example 1: 获取特征向量**



Input: 

```
tccli lke GetEmbedding --cli-unfold-argument  \
    --Model lke-text-embedding-v1 \
    --Inputs 你好 \
    --Online False
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Embedding": [
                    0
                ]
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Usage": {
            "TotalTokens": 3
        }
    }
}
```

