**Example 1: DescribeTLogInfo告警中心概况查询**



Input: 

```
tccli cfw DescribeTLogInfo --cli-unfold-argument  \
    --EndTime 2021-09-18 12:00:00 \
    --SearchValue {country: 1, instance_id:instanceidtest, source:1} \
    --QueryType 1 \
    --StartTime 2021-09-17 12:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "OutNum": 1,
            "HandleNum": 112,
            "NetworkNum": 6,
            "VulNum": 629,
            "BanNum": 0,
            "BruteForceNum": 0
        },
        "RequestId": "706bdce3-bdc4-4cfe-8672-ed08cb451ef1"
    }
}
```

