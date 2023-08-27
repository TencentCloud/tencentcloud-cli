**Example 1: DescribeTRTCRealTimeScaleData**

查询在线TRTC房间和用户

Input: 

```
tccli trtc DescribeTRTCRealTimeScaleData --cli-unfold-argument  \
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
                        "abc"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                0
                            ]
                        }
                    ]
                }
            ],
            "Total": 0
        },
        "RequestId": "abc"
    }
}
```

