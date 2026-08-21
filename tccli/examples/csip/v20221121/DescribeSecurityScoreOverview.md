**Example 1: 获取安全评分概览**



Input: 

```
tccli csip DescribeSecurityScoreOverview --cli-unfold-argument  \
    --MemberId mem-*********************429
```

Output: 
```
{
    "Response": {
        "Score": 85,
        "Level": "good",
        "ScoreStatus": "success",
        "InitialScore": 100,
        "RiskCategoryCount": 3,
        "DeductScore": 15,
        "CalculatedAt": "2026-07-18T10:30:00+08:00",
        "Dimensions": [],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

