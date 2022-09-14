**Example 1: 七层时序流量数据查询接口示例**



Input: 

```
tccli teo DescribeOverviewL7Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_request
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Max": 8037,
                        "Sum": 48511,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 1
                            },
                            {
                                "Timestamp": 1659225600,
                                "Value": 2
                            }
                        ],
                        "DetailData": [
                            1,
                            2,
                            3
                        ],
                        "Avg": 1564,
                        "MetricName": "l7Flow_outFlux"
                    }
                ]
            }
        ],
        "Interval": "5min",
        "Type": "user",
        "RequestId": "6cc74d08-c174-413a-976b-abe7b851e010"
    }
}
```

