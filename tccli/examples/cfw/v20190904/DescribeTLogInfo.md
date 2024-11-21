**Example 1: DescribeTLogInfo告警中心概况查询**

DescribeTLogInfo告警中心概况查询

Input: 

```
tccli cfw DescribeTLogInfo --cli-unfold-argument  \
    --EndTime 2024-10-31 15:06:18 \
    --QueryType 1 \
    --SearchValue {"instance_id":"ins-id"} \
    --StartTime 2024-10-01 15:06:18
```

Output: 
```
{
    "Response": {
        "Data": {
            "BanNum": 0,
            "BruteForceNum": 0,
            "HandleNum": 0,
            "NetworkNum": 90,
            "OutNum": 6,
            "VulNum": 5751
        },
        "RequestId": "da5ee2e0-935e-4b82-8a57-610a6255d5a9"
    }
}
```

