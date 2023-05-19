**Example 1: 日志审计日志查询**

日志审计日志查询

Input: 

```
tccli cfw DescribeLogs --cli-unfold-argument  \
    --Filters.0.Name protocol \
    --Filters.0.Values ANY TCP ICMP \
    --Filters.0.OperatorType 1 \
    --Limit 10 \
    --Offset 0 \
    --Index netflow_border \
    --StartTime 2021-09-21 12:00:00 \
    --EndTime 2021-09-21 12:00:00
```

Output: 
```
{
    "Response": {
        "Data": "[]",
        "RequestId": "e368c536-0331-46d3-b888-90c27152970f",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 0
    }
}
```

