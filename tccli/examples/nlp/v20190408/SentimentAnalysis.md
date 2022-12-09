**Example 1: 情感分析示例**



Input: 

```
tccli nlp SentimentAnalysis --cli-unfold-argument  \
    --Text 今天受了委屈，心情很差。 \
    --Mode 3class
```

Output: 
```
{
    "Response": {
        "Neutral": 9.115e-05,
        "Negative": 0.99992788,
        "RequestId": "2d938c8b-d4cf-4b4e-9c1b-b587eb56d602",
        "Positive": 1.098e-05,
        "Sentiment": "negative"
    }
}
```

