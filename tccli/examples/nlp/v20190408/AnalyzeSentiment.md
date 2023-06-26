**Example 1: 情感分析调用示例**

情感分析。

Input: 

```
tccli nlp AnalyzeSentiment --cli-unfold-argument  \
    --Text 我真开心。
```

Output: 
```
{
    "Response": {
        "Negative": 0.004367333836853504,
        "Neutral": 0.06927284598350525,
        "Positive": 0.9263598322868347,
        "RequestId": "848b909b-5ed7-44ad-b4d0-72bcf0be4f2a",
        "Sentiment": "positive"
    }
}
```

