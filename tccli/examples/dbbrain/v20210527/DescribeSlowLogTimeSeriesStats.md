**Example 1: 获取慢日志统计柱状图**



Input: 

```
tccli dbbrain DescribeSlowLogTimeSeriesStats --cli-unfold-argument  \
    --InstanceId test \
    --StartTime '2019-01-01 00:00:00' \
    --EndTime '2019-01-01 01:00:00'
```

Output: 
```
{
    "Response": {
        "TimeSeries": [
            {
                "Count": 0,
                "Timestamp": 1568113800
            },
            {
                "Count": 0,
                "Timestamp": 1568191680
            },
            {
                "Count": 0,
                "Timestamp": 1568269560
            },
            {
                "Count": 0,
                "Timestamp": 1568347440
            },
            {
                "Count": 2,
                "Timestamp": 1568425320
            },
            {
                "Count": 0,
                "Timestamp": 1568503200
            },
            {
                "Count": 0,
                "Timestamp": 1568581080
            },
            {
                "Count": 0,
                "Timestamp": 1568658960
            },
            {
                "Count": 0,
                "Timestamp": 1568736840
            },
            {
                "Count": 0,
                "Timestamp": 1568814720
            },
            {
                "Count": 0,
                "Timestamp": 1568892600
            },
            {
                "Count": 0,
                "Timestamp": 1568970480
            },
            {
                "Count": 0,
                "Timestamp": 1569048360
            },
            {
                "Count": 0,
                "Timestamp": 1569126240
            },
            {
                "Count": 0,
                "Timestamp": 1569204120
            },
            {
                "Count": 0,
                "Timestamp": 1569282000
            },
            {
                "Count": 0,
                "Timestamp": 1569359880
            },
            {
                "Count": 0,
                "Timestamp": 1569437760
            },
            {
                "Count": 0,
                "Timestamp": 1569515640
            },
            {
                "Count": 0,
                "Timestamp": 1569593520
            },
            {
                "Count": 0,
                "Timestamp": 1569671400
            },
            {
                "Count": 0,
                "Timestamp": 1569749280
            },
            {
                "Count": 0,
                "Timestamp": 1569827160
            },
            {
                "Count": 0,
                "Timestamp": 1569905040
            },
            {
                "Count": 0,
                "Timestamp": 1569982920
            },
            {
                "Count": 0,
                "Timestamp": 1570060800
            },
            {
                "Count": 0,
                "Timestamp": 1570138680
            },
            {
                "Count": 0,
                "Timestamp": 1570216560
            },
            {
                "Count": 0,
                "Timestamp": 1570294440
            },
            {
                "Count": 0,
                "Timestamp": 1570372320
            },
            {
                "Count": 0,
                "Timestamp": 1570450200
            }
        ],
        "SeriesData": {
            "Series": [
                {
                    "Values": [
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0,
                        1.0
                    ],
                    "Metric": "cpu_use_rate",
                    "Unit": "%"
                }
            ],
            "Timestamp": [
                1568113800,
                1568191680,
                1568269560,
                1568347440,
                1568425320,
                1568503200,
                1568581080,
                1568658960,
                1568736840,
                1568814720,
                1568892600,
                1568970480,
                1569048360,
                1569126240,
                1569204120,
                1569282000,
                1569359880,
                1569437760,
                1569515640,
                1569593520,
                1569671400,
                1569749280,
                1569827160,
                1569905040,
                1569982920,
                1570060800,
                1570138680,
                1570216560,
                1570294440,
                1570372320,
                1570450200
            ]
        },
        "RequestId": "b445f8ee-9357-4d93-83c2-3596f9d1f27e",
        "Period": 77880
    }
}
```

