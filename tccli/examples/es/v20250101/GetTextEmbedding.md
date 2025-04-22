**Example 1: 获取特征向量**



Input: 

```
tccli es GetTextEmbedding --cli-unfold-argument  \
    --ModelName bge-large-zh-v1.5 \
    --Texts 你好
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Embedding": [
                    -0.007741480600088835,
                    -0.017921222373843193,
                    -0.04486401379108429,
                    -0.0073757413774728775,
                    0.014934351667761803,
                    -0.025723660364747047,
                    0.03559861704707146,
                    -0.034379489719867706,
                    0.027674268931150436,
                    0.04876523092389107,
                    -0.04266957566142082
                ],
                "Index": 0
            }
        ],
        "RequestId": "8750abd0-feab-4249-ba96-2df9a14c7202",
        "Usage": {
            "TotalTokens": 2
        }
    }
}
```

