**Example 1: DescribeTRTCRealTimeScaleMetricData**

查询在线TRTC房间和用户

Input: 

```
tccli trtc DescribeTRTCRealTimeScaleMetricData --cli-unfold-argument  \
    --StartTime 1665747036 \
    --EndTime 1665747284 \
    --SdkAppId 1400188366
```

Output: 
```
{
    "Response": {
        "Data": {
            "StatementID": 0,
            "Series": [
                {
                    "Columns": [
                        "time",
                        "userCount",
                        "roomCount"
                    ],
                    "Values": [
                        1681280600,
                        1,
                        1
                    ]
                }
            ],
            "Total": 0
        },
        "RequestId": "abc"
    }
}
```

