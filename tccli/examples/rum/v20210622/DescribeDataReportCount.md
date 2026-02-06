**Example 1: 获取上报量**



Input: 

```
tccli rum DescribeDataReportCount --cli-unfold-argument  \
    --EndTime 1625454840 \
    --ReportType custom \
    --ID 1 \
    --StartTime 1625444040
```

Output: 
```
{
    "Response": {
        "Result": "{\"request_id\":\"65a8fec7-2b39-4b11-893f-3715279d235f\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"},{\"statement_id\":1,\"total\":0,\"offset\":\"\"}]}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

