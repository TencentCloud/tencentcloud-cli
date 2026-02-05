**Example 1: 查询全部站点的七层回源数据**

查询全部站点下所有域名 2025-12-01T00:00:00Z ～ 2025-12-02T00:00:00Z 期间 l7Flow_outFlux_hy 指标的汇总数据。

Input: 

```
tccli teo DescribeTimingL7OriginPullData --cli-unfold-argument  \
    --ZoneIds * \
    --MetricNames l7Flow_outFlux_hy \
    --StartTime 2025-12-01T00:00:00Z \
    --EndTime 2025-12-02T00:00:00Z
```

Output: 
```
{
    "Response": {
        "TimingDataRecords": [
            {
                "TypeKey": "1300224863",
                "TypeValue": [
                    {
                        "Avg": 157,
                        "Detail": [
                            {
                                "Timestamp": 1764547200,
                                "Value": 0
                            }
                        ],
                        "Max": 4643,
                        "MetricName": "l7Flow_outFlux_hy",
                        "Sum": 45461
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "853e9004-b4b0-4ae8-8a8f-510fe42f01e2"
    }
}
```

