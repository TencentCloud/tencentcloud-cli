**Example 1: 查询指定站点在指定计费大区的内容加速流量**

查询指定 zone-id 在指定 region-id 下的内容加速流量计费用量，查询时间粒度为天。

Input: 

```
tccli teo DescribeBillingData --cli-unfold-argument  \
    --StartTime 2024-01-01T00:00:00+08:00 \
    --EndTime 2024-01-24T03:20:00+08:00 \
    --Interval day \
    --MetricName acc_flux \
    --Filters.0.Type region-id \
    --Filters.0.Value MidEast \
    --ZoneIds zone-2smdfso9dr58
```

Output: 
```
{
    "Response": {
        "RequestId": "457e8933-4296-4878-9a7f-fb888559e29e",
        "Data": [
            {
                "Time": "2023-12-31T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-01T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-02T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-03T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-04T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-05T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-06T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-07T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-08T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-09T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-10T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-11T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-12T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-13T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-14T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-15T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-16T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-17T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-18T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-19T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-20T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-21T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-22T16:00:00Z",
                "Value": 0
            },
            {
                "Time": "2024-01-23T16:00:00Z",
                "Value": 0
            }
        ]
    }
}
```

