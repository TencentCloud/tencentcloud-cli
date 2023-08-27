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
                        "userCount",
                        "roomCount"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1692935050,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935060,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935070,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935080,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935090,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935100,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935110,
                                1,
                                1
                            ]
                        },
                        {
                            "RowValue": [
                                1692935120,
                                1,
                                1
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

