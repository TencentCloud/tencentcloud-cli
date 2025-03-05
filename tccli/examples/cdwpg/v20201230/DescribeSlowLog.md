**Example 1: 慢日志查询**

慢日志查询

Input: 

```
tccli cdwpg DescribeSlowLog --cli-unfold-argument  \
    --InstanceId 1abc \
    --StartTime 2012-12-12 12:12:12 \
    --EndTime 2012-12-12 13:12:12 \
    --Limit 0 \
    --Offset 0 \
    --Database 1abc \
    --OrderBy 1abc \
    --OrderByType 1abc \
    --Duration 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "SlowLogDetails": {
            "TotalTime": 0,
            "TotalCallTimes": 0,
            "NormalQuerys": [
                {
                    "CallTimes": 0,
                    "SharedReadBlocks": 0,
                    "SharedWriteBlocks": 0,
                    "DatabaseName": "1abc",
                    "NormalQuery": "1abc",
                    "MaxElapsedQuery": "1abc",
                    "CostTime": 0,
                    "ClientIp": "1abc",
                    "UserName": "1abc",
                    "TotalCallTimesPercent": 0,
                    "TotalCostTimePercent": 0,
                    "MinCostTime": 0,
                    "MaxCostTime": 0,
                    "FirstTime": "2012-12-12 12:12:12",
                    "LastTime": "2012-12-12 12:12:12",
                    "ReadCostTime": 0,
                    "WriteCostTime": 0
                }
            ]
        },
        "RequestId": "1abc"
    }
}
```

