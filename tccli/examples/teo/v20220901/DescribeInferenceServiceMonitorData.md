**Example 1: 查询推理服务的指定监控指标数据**



Input: 

```
tccli teo DescribeInferenceServiceMonitorData --cli-unfold-argument  \
    --ZoneId zone-3lwrlet3u8bl \
    --ServiceIds inf-n40ehcni5jjx \
    --MetricNames cpu_usage_average \
    --StartTime 2026-02-26T15:00:00+08:00 \
    --EndTime 2026-02-26T15:01:00+08:00 \
    --Interval min
```

Output: 
```
{
    "Response": {
        "InferenceServiceMonitorRecords": [
            {
                "InferenceServiceMonitorItems": [
                    {
                        "Timestamp": "2026-02-26T15:00:00+08:00",
                        "Value": 0.005829864994190321
                    }
                ],
                "MetricName": "cpu_usage_average",
                "ServiceId": "inf-n40ehcni5jjx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8fc9f37f-20c1-4d60-818f-a8aa045bf7d5"
    }
}
```

