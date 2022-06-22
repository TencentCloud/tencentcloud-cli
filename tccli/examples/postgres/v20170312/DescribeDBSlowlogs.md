**Example 1: 获取实例慢查询日志**



Input: 

```
tccli postgres DescribeDBSlowlogs --cli-unfold-argument  \
    --EndTime 2018-06-11 17:06:38 \
    --DBInstanceId postgres-apzvwncr \
    --StartTime 2018-06-10 17:06:38
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Detail": {
            "TotalTime": 0.0,
            "NormalQueries": [
                {
                    "UserName": "user",
                    "MaxCostTime": 0.0,
                    "Rows": 0,
                    "CostTime": 0.0,
                    "SharedReadBlks": 0,
                    "Calls": 0,
                    "WriteCostTime": 0,
                    "ReadCostTime": 0,
                    "CallsGrids": [
                        0
                    ],
                    "NormalQuery": "xx",
                    "MinCostTime": 0.0,
                    "DatabaseName": "xx",
                    "FirstTime": "xx",
                    "LastTime": "xx",
                    "SharedWriteBlks": 0
                }
            ],
            "TotalCalls": 0
        },
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

