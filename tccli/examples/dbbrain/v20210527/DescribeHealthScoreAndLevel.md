**Example 1: 获取健康得分以及性能异常详情**

获取健康得分以及性能异常详情

Input: 

```
tccli dbbrain DescribeHealthScoreAndLevel --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --Product mysql \
    --StartTime 2021-02-01T14:30:00+00:00 \
    --EndTime 2021-02-01T14:50:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "698aed27-2780-4904-8d22-e0e3e0f95146",
        "Data": {
            "HealthScore": 100,
            "Metric": "health_score",
            "HealthLevel": "HEALTH",
            "Unit": "分",
            "TimeRangeHealthScore": {
                "PerformanceHealthScoreMin": 83,
                "PerformanceHealthLevelMin": "SUB_HEALTH",
                "HealthScoreMin": 83,
                "HealthLevelMin": "SUB_HEALTH"
            }
        }
    }
}
```

