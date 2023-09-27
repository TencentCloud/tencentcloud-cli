**Example 1: DescribeTRTCMarketScaleData**

查询TRTC数据大盘规模数据

Input: 

```
tccli trtc DescribeTRTCMarketScaleData --cli-unfold-argument  \
    --SdkAppId 1400xxxxxx \
    --StartTime 2023-09-20 \
    --EndTime 2023-09-23 \
    --Period d
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
                        "peakCurrentUsers",
                        "peakCurrentChannels",
                        "userCount",
                        "roomCount"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1695139200,
                                55,
                                37,
                                784,
                                572
                            ]
                        },
                        {
                            "RowValue": [
                                1695225600,
                                62,
                                46,
                                848,
                                614
                            ]
                        },
                        {
                            "RowValue": [
                                1695312000,
                                47,
                                45,
                                950,
                                695
                            ]
                        },
                        {
                            "RowValue": [
                                1695398400,
                                36,
                                35,
                                378,
                                313
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "kp38ibciayx-elqqjdfrf7umkvpbvowt"
    }
}
```

