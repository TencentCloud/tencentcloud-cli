**Example 1: demo**



Input: 

```
tccli rum DescribeDataReportCountV2 --cli-unfold-argument  \
    --EndTime 1625454840 \
    --ReportType custom \
    --ID 1 \
    --StartTime 1625444040
```

Output: 
```
{
    "Response": {
        "Result": "{\"request_id\":\"4d50a7e7-cb3a-47af-a4ff-f545bfd54880\",\"results\":[{\"statement_id\":1,\"series\":[{\"name\":\"log_url_statistics\",\"columns\":[\"time\",\"allCount\"],\"values\":[],\"total\":1,\"offset\":\"\"}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

