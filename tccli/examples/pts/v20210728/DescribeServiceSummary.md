**Example 1: 查询服务汇总信息**



Input: 

```
tccli pts DescribeServiceSummary --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobId 123 \
    --ScenarioId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "f9byccyy7i7u9cw-81axnla-a-ezcnwr",
        "ServiceSummarySet": [
            {
                "Service": "http://pets.com/0",
                "Method": "get",
                "Status": "400",
                "Result": "BadRequest",
                "Count": 41253,
                "Average": 0.4976391081807893,
                "P90": 0.909354130052724,
                "P95": 0.949354130052724,
                "P99": 0.9898708260105447,
                "Min": 0.2198708260105447,
                "Max": 0.9998708260105447
            },
            {
                "Service": "http://pets.com/10",
                "Method": "get",
                "Status": "400",
                "Result": "BadRequest",
                "Count": 41252,
                "Average": 0.49687854602238934,
                "P90": 0.909354130052724,
                "P95": 0.949698900331646,
                "P99": 0.9899397800663291,
                "Min": 0.2198708260105447,
                "Max": 0.9998708260105447
            }
        ]
    }
}
```

