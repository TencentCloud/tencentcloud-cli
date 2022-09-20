**Example 1: 查询四层时序流量数据**



Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l4Flow_inFlux
```

Output: 
```
{
    "Response": {
        "RequestId": "e12e0659-ae34-4140-9878-4a61db0c3639",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 740563,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1659225600,
                                "Value": 0
                            }
                        ],
                        "Max": 6319079,
                        "MetricName": "l4Flow_inFlux",
                        "Sum": 22957455
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

