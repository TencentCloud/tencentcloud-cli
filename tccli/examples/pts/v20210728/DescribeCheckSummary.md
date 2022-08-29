**Example 1: 查询检查点汇总信息**



Input: 

```
tccli pts DescribeCheckSummary --cli-unfold-argument  \
    --ProjectId xx \
    --ScenarioId xx \
    --JobId xx
```

Output: 
```
{
    "Response": {
        "CheckSummarySet": [
            {
                "Name": "400",
                "Step": "sample",
                "SuccessCount": 0,
                "FailCount": 92343,
                "ErrorRate": 1
            },
            {
                "Name": "status 200",
                "Step": "sample",
                "SuccessCount": 831084,
                "FailCount": 0,
                "ErrorRate": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

