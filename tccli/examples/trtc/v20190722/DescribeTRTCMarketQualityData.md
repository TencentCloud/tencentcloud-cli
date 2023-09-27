**Example 1: DescribeTRTCMarketQualityData**

查询TRTC数据大盘质量相关数据

Input: 

```
tccli trtc DescribeTRTCMarketQualityData --cli-unfold-argument  \
    --SdkAppId 1400xxxxxx \
    --StartTime 2020-09-22 \
    --EndTime 2020-09-22 \
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
                        "videoFreezeRate",
                        "audioFreezeRate",
                        "networkDelay",
                        "joinSuccessRate",
                        "joinSuccessRate"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1664553600,
                                2,
                                0,
                                0,
                                97,
                                97
                            ]
                        },
                        {
                            "RowValue": [
                                1664640000,
                                3,
                                0,
                                0,
                                98,
                                98
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

