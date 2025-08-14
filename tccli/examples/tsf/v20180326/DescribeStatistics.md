**Example 1: test**



Input: 

```
tccli tsf DescribeStatistics --cli-unfold-argument  \
    --OrderBy AvgTimeConsuming \
    --StartTime 2020-05-12 14:43:12 \
    --TimeStep 1 \
    --Offset 1 \
    --DbName mysql \
    --ServiceName demo-service \
    --Limit 1 \
    --SearchWord keyword \
    --OrderType 1 \
    --EndTime 2020-05-12 14:43:12 \
    --Type Service \
    --NamespaceId namespace-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b057eeaa-ccdf-40be-995f-f059b4b974e8",
        "Result": {
            "TotalCount": 2,
            "Content": []
        }
    }
}
```

