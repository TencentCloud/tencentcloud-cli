**Example 1: 获取特征向量**



Input: 

```
tccli lke GetEmbedding --cli-unfold-argument  \
    --Model doc-normal-500-v5.8 \
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
        "RequestId": "abc"
    }
}
```

