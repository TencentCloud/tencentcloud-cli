**Example 1: 获取DNS请求数统计曲线**



Input: 

```
tccli teo DescribeDnsData --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:01:00+00:00 \
    --Filters.0.Name zone \
    --Filters.0.Value a.com
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

