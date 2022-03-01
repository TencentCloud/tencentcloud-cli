**Example 1: 服务统计**



Input: 

```
tccli tsf DescribeStatistics --cli-unfold-argument  \
    --NamespaceId "test" \
    --Type "test" \
    --TimeStep 60 \
    --OrderBy "AvgTimeConsuming" \
    --StartTime '2020-06-02 16:37:30' \
    --EndTime '2020-06-02 17:37:30' \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "4517c1fc-3c2b-44fa-a7c8-aa45b6c91ed6",
        "Result": {
            "TotalCount": 0,
            "Content": null
        }
    }
}
```

