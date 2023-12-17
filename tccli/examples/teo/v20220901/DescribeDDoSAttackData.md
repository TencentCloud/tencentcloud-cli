**Example 1: 查询DDoS攻击时序数据**



Input: 

```
tccli teo DescribeDDoSAttackData --cli-unfold-argument  \
    --MetricNames ddos_attackMaxBandwidth \
    --Interval min \
    --PolicyIds 1706 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2022-08-22T00:00:00+00:00 \
    --EndTime 2022-08-23T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Value": [
                    {
                        "Max": 100,
                        "Metric": "ddos_attackMaxBandwidth",
                        "Avg": 100.0,
                        "Detail": [
                            {
                                "Timestamp": 1660010100,
                                "Value": 100
                            }
                        ],
                        "Sum": 100.0
                    }
                ],
                "Key": "ddos_attackMaxBandwidth"
            }
        ],
        "RequestId": "a79e60f8-34cc-4ee5-a7f9-a24adb572c68"
    }
}
```

