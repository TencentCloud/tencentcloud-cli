**Example 1: 重排序**

重排序

Input: 

```
tccli lkeap RunRerank --cli-unfold-argument  \
    --Query 知识引擎大模型 \
    --Docs 混元大模型 腾讯知识引擎
```

Output: 
```
{
    "Response": {
        "RequestId": "766383fd-5219-4d13-aa1a-7ae00766640c",
        "ScoreList": [
            -9.006162,
            2.8577538
        ],
        "Usage": {
            "TotalTokens": 27
        }
    }
}
```

