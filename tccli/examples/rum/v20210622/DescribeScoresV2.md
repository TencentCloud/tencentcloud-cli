**Example 1: demo**



Input: 

```
tccli rum DescribeScoresV2 --cli-unfold-argument  \
    --StartTime 2025080100 \
    --EndTime 2025081000
```

Output: 
```
{
    "Response": {
        "RequestId": "1dfa1684-d91f-479e-899b-b3a14c09afd9",
        "ScoreSet": [
            {
                "ProjectID": 124708,
                "Score": 0,
                "ApiPerformanceScore": 0,
                "ApiAvailableScore": 0,
                "ApiNum": 0,
                "ApiFail": 0,
                "ApiDuration": 0,
                "PagePerformanceScore": 0,
                "PagePv": 0,
                "PageUv": 0,
                "PageError": 0,
                "PageDuration": 0,
                "PageLCP": 0,
                "PageFID": 0,
                "PageCLS": 0,
                "PageFCP": 0,
                "PageINP": 0,
                "JsErrorScore": 0,
                "StaticAvailableScore": 0,
                "StaticPerformanceScore": 0,
                "StaticNum": 0,
                "StaticFail": 0,
                "StaticDuration": 0
            }
        ]
    }
}
```

