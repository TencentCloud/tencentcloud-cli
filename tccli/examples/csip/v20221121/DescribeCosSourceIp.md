**Example 1: 调用源ip列表**



Input: 

```
tccli csip DescribeCosSourceIp --cli-unfold-argument  \
    --Filter.Filters.0.Name IpType \
    --Filter.Filters.0.Values 2 \
    --Filter.Filters.0.OperatorType 1 \
    --Filter.Offset 0 \
    --Filter.Limit 20 \
    --Filter.Order desc \
    --Filter.By LastAccessTime \
    --Filter.StartTime 2024-01-01 00:00:00 \
    --Filter.EndTime 2024-01-31 23:59:59
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "UA": [
                    "cos-console"
                ]
            }
        ],
        "Total": 156,
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

