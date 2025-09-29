**Example 1: 获取特征向量**



Input: 

```
tccli lkeap GetEmbedding --cli-unfold-argument  \
    --Model lke-text-embedding-v1 \
    --Inputs 你好
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

**Example 2: 获取特征向量v2**



Input: 

```
tccli lkeap GetEmbedding --cli-unfold-argument  \
    --Model lke-text-embedding-v2 \
    --Inputs 1 \
    --TextType document \
    --Instruction 问题:
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Embedding": [
                    0.009212733
                ]
            }
        ],
        "Usage": {
            "TotalTokens": 3
        },
        "RequestId": "d4b6b8fb-597c-43f3-860d-715916c787b8"
    }
}
```

