**Example 1: 情感分析示例**



Input: 

```
tccli nlp SentimentAnalysis --cli-unfold-argument  \
    --Text "今天受了委屈，心情很差。"\
    --Flag 2
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "Neutral": null,
        "Sentiment": "negative",
        "Positive": 0.03649453,
        "Negative": 0.96350545
    }
}
```

