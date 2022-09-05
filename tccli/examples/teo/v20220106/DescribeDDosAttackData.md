**Example 1: 查询DDos攻击时序数据**



Input: 

```
tccli teo DescribeDDosAttackData --cli-unfold-argument  \
    --AttackType UDPFLOOD \
    --MetricNames ddos_attackMaxBandwidth \
    --ProtocolType udp \
    --Interval min \
    --PolicyIds 1706 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2022-08-22T00:00:00+00:00 \
    --EndTime 2022-08-23T00:00:00+00:00 \
    --Port 22 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Msg": "success",
        "Interval": "min",
        "Data": [
            {
                "Value": [
                    {
                        "Max": 100,
                        "Metric": "ddos_attackMaxBandwidth",
                        "Avg": 100.0,
                        "Detail": [
                            {
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

