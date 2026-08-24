**Example 1: 查询 DDoS 攻击带宽时序数据**

在 ZoneId 为 zone-2psss4drfg29 的站点下，以分钟为数据统计粒度，查询被攻击目的 IP 的 DDoS 攻击带宽时序数据。

Input: 

```
tccli teo DescribeDDoSAttackData --cli-unfold-argument  \
    --StartTime 2025-08-22T00:00:00+00:00 \
    --EndTime 2025-08-22T00:00:59+00:00 \
    --MetricNames ddos_attackBandwidth \
    --ZoneIds zone-2psss4drfg29 \
    --PolicyIds 1706 \
    --Interval min \
    --Filters.0.Key ddos-attack-dip \
    --Filters.0.Operator equals \
    --Filters.0.Value 1**.2*.1**.1*
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "ddos_attackBandwidth",
                "Value": [
                    {
                        "Avg": 100,
                        "Detail": [
                            {
                                "Timestamp": 1755820800,
                                "Value": 100
                            }
                        ],
                        "Max": 100,
                        "Metric": "ddos_attackBandwidth",
                        "Sum": 100
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "60b91eaf-e560-4b59-a388-61d85b637f34"
    }
}
```

