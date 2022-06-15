**Example 1: 七层时序流量数据查询接口示例**



Input: 

```
tccli teo DescribeOverviewL7Data --cli-unfold-argument  \
    --Protocol xx \
    --MetricNames xx \
    --Interval xx \
    --ZoneIds xx \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains xx \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeKey": "xx",
                "TypeValue": [
                    {
                        "Max": 0,
                        "Sum": 0,
                        "Detail": [
                            {
                                "Timestamp": 0,
                                "Value": 0
                            }
                        ],
                        "DetailData": [
                            0
                        ],
                        "Avg": 0,
                        "MetricName": "xx"
                    }
                ]
            }
        ],
        "Interval": "xx",
        "Type": "xx",
        "RequestId": "xx"
    }
}
```

