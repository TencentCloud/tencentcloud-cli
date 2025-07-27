**Example 1: 慢查询统计分析接口实例**

获取指定时间范围内实例的慢查询统计分析结果。


Input: 

```
tccli postgres DescribeSlowQueryAnalysis --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DBInstanceId postgres-1xm16x1d \
    --StartTime 2025-07-21 20:00:00 \
    --EndTime 2025-07-21 21:00:00
```

Output: 
```
{
    "Response": {
        "Detail": {
            "AnalysisItems": [
                {
                    "AvgCostTime": 2016,
                    "CallNum": 1,
                    "CallPercent": 100,
                    "ClientAddr": "11.141.188.142:57346",
                    "CostPercent": 100,
                    "CostTime": 2016,
                    "DatabaseName": "postgres",
                    "FirstTime": "2025-07-21 20:56:13",
                    "LastTime": "2025-07-21 20:56:13",
                    "MaxCostTime": 2016,
                    "MinCostTime": 2016,
                    "NormalQuery": "SELECT pg_sleep($1);",
                    "UserName": "admin"
                }
            ],
            "TotalCallNum": 1,
            "TotalTime": 2016
        },
        "RequestId": "d7436dd0-155d-47c4-9b18-5318019a1706",
        "TotalCount": 1
    }
}
```

