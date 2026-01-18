**Example 1: 查询通道组统计数据**



Input: 

```
tccli gaap DescribeProxyGroupStatistics --cli-unfold-argument  \
    --GroupId lg-0o223et7 \
    --StartTime 2026-01-01 00:00:00 \
    --EndTime 2026-01-01 00:10:00 \
    --MetricNames InBandwidth \
    --Granularity 300
```

Output: 
```
{
    "Response": {
        "StatisticsData": [
            {
                "MetricData": [
                    {
                        "Data": null,
                        "Time": 1767196800
                    }
                ],
                "MetricName": "InBandwidth"
            }
        ],
        "RequestId": "accd1efb-fed9-4c69-b379-50039e5336f1"
    }
}
```

