**Example 1: demo**



Input: 

```
tccli rum DescribeDataPvUrlStatisticsV2 --cli-unfold-argument  \
    --ID 131800 \
    --Type ext3 \
    --StartTime 1745911200 \
    --EndTime 1748427659
```

Output: 
```
{
    "Response": {
        "RequestId": "85acc203-d239-4e47-bc04-195cb09e9e83",
        "Result": "{\"request_id\":\"85acc203-d239-4e47-bc04-195cb09e9e83\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

