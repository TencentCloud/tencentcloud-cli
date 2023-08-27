**Example 1: DescribeTRTCMarketQualityData**

查询TRTC数据大盘质量数据

Input: 

```
tccli trtc DescribeTRTCMarketQualityData --cli-unfold-argument  \
    --SdkAppId abc \
    --StartTime 2020-09-22 \
    --EndTime 2020-09-22 \
    --Period abc
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

