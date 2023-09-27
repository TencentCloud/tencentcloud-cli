**Example 1: DescribeTRTCRealTimeQualityData**

查询TRTC实时监控质量数据

Input: 

```
tccli trtc DescribeTRTCRealTimeQualityData --cli-unfold-argument  \
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
                        "videoFreezeRate",
                        "audioFreezeRate"
                    ],
                    "Values": [
                        {
                            "RowValue": [
                                1695711350,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711360,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711370,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711380,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711390,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711400,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711410,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711420,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711430,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711440,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711450,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711460,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711470,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711480,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711490,
                                0,
                                4
                            ]
                        },
                        {
                            "RowValue": [
                                1695711500,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711510,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711520,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711530,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711540,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711550,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711560,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711570,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711580,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711590,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711600,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711610,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711620,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711630,
                                0,
                                0
                            ]
                        },
                        {
                            "RowValue": [
                                1695711640,
                                0,
                                0
                            ]
                        }
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "75fegcba14mffq3wl2zz578ml3e-i1a3"
    }
}
```

