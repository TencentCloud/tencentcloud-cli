**Example 1: 获取计费用量**



Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:01:00+00:00 \
    --MetricName sec_flux \
    --Interval min \
    --Filters.0.Type zone \
    --Filters.0.Value test.com
```

Output: 
```
{
    "Response": {
        "Interval": "min",
        "RequestId": "xx",
        "Data": [
            {
                "Time": "2020-09-22T00:00:00+00:00",
                "Value": 100
            },
            {
                "Time": "2020-09-22T00:01:00+00:00",
                "Value": 200
            }
        ]
    }
}
```

