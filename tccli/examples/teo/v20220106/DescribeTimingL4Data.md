**Example 1: 四层时序流量数据查询接口示例**



Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --Protocol xx \
    --MetricNames xx \
    --RuleId xx \
    --Interval xx \
    --ZoneIds xx \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --InstanceIds xx
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

