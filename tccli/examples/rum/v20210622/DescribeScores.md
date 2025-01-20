**Example 1: 获取首页Score**

获取首页Score

Input: 

```
tccli rum DescribeScores --cli-unfold-argument  \
    --EndTime 2022051914 \
    --ID 1 \
    --StartTime 2020011920
```

Output: 
```
{
    "Response": {
        "ScoreSet": [
            {
                "ApiAvaliableScore": "30",
                "ApiDuration": "0",
                "ApiFail": "0",
                "ApiNum": "0",
                "ApiPerformanceScore": "5",
                "CreateTime": "",
                "JsErrorScore": "30",
                "PageDuration": "0",
                "PageError": "0",
                "PagePerformanceScore": "10",
                "PagePv": "1",
                "PageUv": "0",
                "ProjectID": 1,
                "RecordNum": 1,
                "Score": "100",
                "StaticAvaliableScore": "20",
                "StaticDuration": "210",
                "StaticFail": "0",
                "StaticNum": "9",
                "StaticPerformanceScore": "5"
            }
        ],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

