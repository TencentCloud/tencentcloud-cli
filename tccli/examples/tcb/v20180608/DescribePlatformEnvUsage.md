**Example 1: 查询环境资源用量**



Input: 

```
tccli tcb DescribePlatformEnvUsage --cli-unfold-argument  \
    --EnvId jeff-d4g6izo8z6a0502f6 \
    --StartDate 2026-08-20 \
    --EndDate 2026-09-20 \
    --ResourceTypes Storage \
    --NeedUsageDetails True
```

Output: 
```
{
    "Response": {
        "CreditsScale": 10000,
        "Resources": [
            {
                "Metrics": [
                    {
                        "Credits": 50000,
                        "DailyUsageList": [
                            {
                                "Credits": 50000,
                                "Date": "2026-09-08",
                                "UsageValue": 5000
                            }
                        ],
                        "MetricName": "ReadRequests",
                        "OriginalMetricName": "ReadRequests",
                        "OriginalResourceType": "COS",
                        "UsageUnit": "Count",
                        "UsageValue": 5000
                    }
                ],
                "ResourceType": "Storage",
                "TotalCredits": 100000
            }
        ],
        "TotalCredits": 100000,
        "RequestId": "b847eba1-a5b0-4f2a-b978-cc0389ca5141"
    }
}
```

