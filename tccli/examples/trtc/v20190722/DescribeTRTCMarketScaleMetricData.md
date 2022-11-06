**Example 1: DescribeTRTCMarketScaleMetricData**



Input: 

```
tccli trtc DescribeTRTCMarketScaleMetricData --cli-unfold-argument  \
    --StartTime 2022-10-01 \
    --EndTime 2022-10-13 \
    --Period d \
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
                        "roomCount",
                        "peakCurrentChannels",
                        "peakCurrentUsers"
                    ],
                    "Values": [
                        [
                            1664553600,
                            16,
                            12,
                            0,
                            0
                        ],
                        [
                            1664640000,
                            17,
                            13,
                            0,
                            0
                        ],
                        [
                            1664726400,
                            14,
                            11,
                            0,
                            0
                        ],
                        [
                            1664812800,
                            16,
                            12,
                            0,
                            0
                        ],
                        [
                            1664899200,
                            17,
                            12,
                            0,
                            0
                        ],
                        [
                            1664985600,
                            17,
                            12,
                            0,
                            0
                        ],
                        [
                            1665072000,
                            16,
                            14,
                            0,
                            0
                        ],
                        [
                            1665158400,
                            29,
                            21,
                            0,
                            0
                        ],
                        [
                            1665244800,
                            43,
                            32,
                            0,
                            0
                        ],
                        [
                            1665331200,
                            42,
                            32,
                            0,
                            0
                        ],
                        [
                            1665417600,
                            47,
                            31,
                            0,
                            0
                        ],
                        [
                            1665504000,
                            51,
                            35,
                            0,
                            0
                        ],
                        [
                            1665590400,
                            49,
                            34,
                            0,
                            0
                        ]
                    ]
                }
            ],
            "Total": 1
        },
        "RequestId": "mg--88gg8wpzr8j26-2wl1xk4pmqfanw"
    }
}
```

