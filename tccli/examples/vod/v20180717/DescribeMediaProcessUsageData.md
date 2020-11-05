**Example 1: Querying video processing usage**



Input: 

```
tccli vod DescribeMediaProcessUsageData --cli-unfold-argument  \
    --StartTime 2019-07-02T00:00:00+08:00\
    --EndTime 2019-07-03T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "MediaProcessDataSet": [
            {
                "TaskType": "Transcode",
                "Summary": [
                    {
                        "Time": "2019-07-02T00:00:00+08:00",
                        "Count": 3,
                        "Usage": 30
                    },
                    {
                        "Time": "2019-07-03T00:00:00+08:00",
                        "Count": 3,
                        "Usage": 30
                    }
                ],
                "Details": [
                    {
                        "Specification": "Audio",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    },
                    {
                        "Specification": "Standard.H264.HD",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    },
                    {
                        "Specification": "TESHD-10.H265.4K",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "requestId"
    }
}
```

