**Example 1: 七层数据分析类top流量数据接口**

七层数据分析类top流量数据接口

Input: 

```
tccli teo DescribeTopL7CacheData --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Interval xx \
    --ZoneIds xx \
    --Limit 0 \
    --Filters.0.Operator xx \
    --Filters.0.Value xx \
    --Filters.0.Key xx \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --MetricName xx
```

Output: 
```
{
    "Response": {
        "Type": "xx",
        "Data": {
            "DetailData": [
                {
                    "Value": 3000,
                    "Key": "xx"
                },
                {
                    "Key": "xx",
                    "Value": 5000
                },
                {
                    "Key": "xx",
                    "Value": 8000
                }
            ],
            "TypeKey": "xx"
        },
        "RequestId": "xx",
        "MetricName": "xx"
    }
}
```

