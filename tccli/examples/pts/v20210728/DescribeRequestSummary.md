**Example 1: 查询请求汇总信息**



Input: 

```
tccli pts DescribeRequestSummary --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobId 123 \
    --ScenarioId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RequestSummarySet": [
            {
                "Service": "http://pets.com/0",
                "Method": "get",
                "ErrorPercentage": 1,
                "Count": 41253,
                "Average": 0.4976391081807893,
                "P90": 0.909354130052724,
                "P95": 0.949354130052724,
                "Min": 0.2198708260105447,
                "Max": 0.9998708260105447
            },
            {
                "Service": "http://pets.com/10",
                "Method": "get",
                "ErrorPercentage": 1,
                "Count": 41252,
                "Average": 0.49687854602238934,
                "P90": 0.909354130052724,
                "P95": 0.949698900331646,
                "Min": 0.2198708260105447,
                "Max": 0.9998708260105447
            }
        ]
    }
}
```

