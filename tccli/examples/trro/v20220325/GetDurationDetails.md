**Example 1: 时长明细**



Input: 

```
tccli trro GetDurationDetails --cli-unfold-argument  \
    --StartTime 1703433600 \
    --EndTime 1703443600 \
    --ProjectId m82k5408n675phvb \
    --DeviceId dev1 \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1ab8afa4-4d7c-842e-ff00-b9893318fef0",
        "DurationDetails": [
            {
                "SessionTime": "1719331200",
                "Voice": 0,
                "SD": 0,
                "HD": 3240,
                "FHD": 0,
                "TwoK": 0,
                "FourK": 0,
                "Online": 432
            }
        ],
        "TotalCount": 1
    }
}
```

