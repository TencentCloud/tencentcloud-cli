**Example 1: demo**



Input: 

```
tccli rum DescribeDataLogUrlStatisticsV2 --cli-unfold-argument  \
    --ID 131800 \
    --Type ext3 \
    --StartTime 1745911200 \
    --EndTime 1748427659
```

Output: 
```
{
    "Response": {
        "RequestId": "97e9e8cc-e106-4034-889c-c8f8d3451057",
        "Result": "{\"request_id\":\"97e9e8cc-e106-4034-889c-c8f8d3451057\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

