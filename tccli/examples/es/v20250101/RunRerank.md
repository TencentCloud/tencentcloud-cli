**Example 1: 重排序**



Input: 

```
tccli es RunRerank --cli-unfold-argument  \
    --ModelName bge-rerank-large \
    --Query 你好 \
    --Documents 你好？ 你好。
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Document": "",
                "Index": 1,
                "RelevanceScore": 0.9998511075973511
            },
            {
                "Document": "",
                "Index": 0,
                "RelevanceScore": 0.9996849298477173
            }
        ],
        "RequestId": "cf9c5598-9625-436d-bc81-8dd3900e63c0",
        "Usage": {
            "TotalTokens": 10
        }
    }
}
```

