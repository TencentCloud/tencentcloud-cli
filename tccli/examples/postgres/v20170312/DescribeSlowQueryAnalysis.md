**Example 1: 慢查询统计分析接口实例**



Input: 

```
tccli postgres DescribeSlowQueryAnalysis --cli-unfold-argument  \
    --StartTime 2021-06-17 20:00:07 \
    --EndTime 2021-06-17 20:15:07 \
    --Limit 10 \
    --Offset 0 \
    --DBInstanceId postgres-nbvqjlhf
```

Output: 
```
{
    "Response": {
        "Detail": {
            "AnalysisItems": [
                {
                    "AvgCostTime": 101.01300048828125,
                    "ClientAddr": "",
                    "CostPercent": 11.703700311890035,
                    "CostTime": 101.01300048828125,
                    "DatabaseName": "postgres",
                    "FirstTime": "2021-07-27 03:12:01",
                    "LastTime": "2021-07-27 03:12:01",
                    "MaxCostTime": 101.01300048828125,
                    "MinCostTime": 101.01300048828125,
                    "NormalQuery": "select $1 from information_schema.tables where table_schema = $2 and table_name = $3",
                    "UserName": "postgres"
                }
            ],
            "TotalCallNum": 6,
            "TotalTime": 863.0860137939453
        },
        "RequestId": "221334ddc4f",
        "TotalCount": 5
    }
}
```

