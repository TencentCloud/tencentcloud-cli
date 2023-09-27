**Example 1: DescribeTRTCRealTimeScaleData**

查询在线TRTC房间和用户

Input: 

```
tccli trtc DescribeTRTCRealTimeScaleData --cli-unfold-argument  \
    --StartTime 1695711343 \
    --EndTime 1695711643 \
    --SdkAppId 1400xxxxxx
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
                                1695711350,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711360,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711370,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711380,
                                22,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711390,
                                23,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711400,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711410,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711420,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711430,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711440,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711450,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711460,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711470,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711480,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711490,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711500,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711510,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711520,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711530,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711540,
                                21,
                                18
                            ]
                        },
                        {
                            "RowValue": [
                                1695711550,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711560,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711570,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711580,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711590,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711600,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711610,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711620,
                                22,
                                19
                            ]
                        },
                        {
                            "RowValue": [
                                1695711630,
                                24,
                                20
                            ]
                        },
                        {
                            "RowValue": [
                                1695711640,
                                22,
                                19
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "7gb56tcisiuy9el619p3jjkccop9qpv8"
    }
}
```

