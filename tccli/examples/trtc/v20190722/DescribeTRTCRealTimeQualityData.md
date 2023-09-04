**Example 1: DescribeTRTCRealTimeQualityData**

查询TRTC实时监控质量数据

Input: 

```
tccli trtc DescribeTRTCRealTimeQualityData --cli-unfold-argument  \
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
                        "videoFreezeRate",
                        "audioFreezeRate"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1692935050,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1692935060,
                                0,
                                0
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "4mry45x5sslfsee3vfl5n99oz4u9u-8w"
    }
}
```

