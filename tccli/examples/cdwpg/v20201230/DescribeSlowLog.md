**Example 1: 慢日志查询**

慢日志查询

Input: 

```
tccli cdwpg DescribeSlowLog --cli-unfold-argument  \
    --InstanceId cdwpg-54tsge58 \
    --StartTime 2025-03-10 12:12:12 \
    --EndTime 2025-03-25 16:12:12
```

Output: 
```
{
    "Response": {
        "RequestId": "d6ea55cc-1ddb-4c9f-99c9-ea7907cedacc",
        "SlowLogDetails": {
            "NormalQuerys": [
                {
                    "CallTimes": 1,
                    "ClientIp": "9.0.116.10",
                    "CostTime": 10403.899,
                    "DatabaseName": "evidev",
                    "FirstTime": "2025-03-25 12:07:49",
                    "LastTime": "2025-03-25 12:07:49",
                    "MaxCostTime": 10403.899,
                    "MaxElapsedQuery": "insert into row1 select * from row1;",
                    "MinCostTime": 10403.899,
                    "NormalQuery": "insert into row1 select * from row1;",
                    "ReadCostTime": 0,
                    "SharedReadBlocks": 0,
                    "SharedWriteBlocks": 0,
                    "TotalCallTimesPercent": 1,
                    "TotalCostTimePercent": 1,
                    "UserName": "dbadmin",
                    "WriteCostTime": 0
                }
            ],
            "TotalCallTimes": 1,
            "TotalTime": 10403.899
        },
        "TotalCount": 1
    }
}
```

