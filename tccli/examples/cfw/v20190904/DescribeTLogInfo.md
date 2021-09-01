**Example 1: DescribeTLogInfo**



Input: 

```
tccli cfw DescribeTLogInfo --cli-unfold-argument  \
    --EndTime xx \
    --SearchValue xx \
    --QueryType xx \
    --StartTime xx
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

