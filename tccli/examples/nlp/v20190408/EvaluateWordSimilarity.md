**Example 1: 词相似度调用示例**

分析词相似度

Input: 

```
tccli nlp EvaluateWordSimilarity --cli-unfold-argument  \
    --SourceWord 香港 \
    --TargetWord 北京
```

Output: 
```
{
    "Response": {
        "RequestId": "02bd6796-515a-452e-a455-23523fd6cfd9",
        "Similarity": 0.5935152769088745
    }
}
```

