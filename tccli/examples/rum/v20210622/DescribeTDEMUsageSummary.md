**Example 1: 查询用量合计**



Input: 

```
tccli rum DescribeTDEMUsageSummary --cli-unfold-argument  \
    --StartTime 2026-09-15 00:00:00 \
    --EndTime 2026-09-22 13:00:00
```

Output: 
```
{
    "Response": {
        "ByDate": [
            {
                "ReportVolume": 50987,
                "Time": "2026-09-15 00:00:00"
            }
        ],
        "Granularity": "day",
        "ReportVolume": 4265974,
        "ResourceCount": 13,
        "RequestId": "8b95c45e-1fe0-46b3-bbf6-3e0aeebebb05"
    }
}
```

