**Example 1: DescribeTLogInfo**



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
            "NetworkNum": 0,
            "HandleNum": 0,
            "BanNum": 0,
            "VulNum": 0,
            "OutNum": 0,
            "BruteForceNum": 0
        },
        "RequestId": "xx"
    }
}
```

