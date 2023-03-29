**Example 1: 查询视频处理用量**

查询视频处理用量

Input: 

```
tccli vod DescribeMediaProcessUsageData --cli-unfold-argument  \
    --EndTime 2020-09-09T23:59:59+08:00 \
    --Type Transcoding-TESHD \
    --StartTime 2020-09-07T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "MediaProcessDataSet": [
            {
                "TaskType": "Transcoding-TESHD",
                "Summary": [
                    {
                        "Time": "2020-09-07T00:00:00+08:00",
                        "Count": 2,
                        "Usage": 26
                    },
                    {
                        "Time": "2020-09-08T00:00:00+08:00",
                        "Count": 2,
                        "Usage": 168
                    },
                    {
                        "Time": "2020-09-09T00:00:00+08:00",
                        "Count": 2,
                        "Usage": 26
                    }
                ],
                "Details": [
                    {
                        "Specification": "TESHD-10.H264.SD",
                        "Data": [
                            {
                                "Time": "2020-09-07T00:00:00+08:00",
                                "Count": 2,
                                "Usage": 26
                            },
                            {
                                "Time": "2020-09-08T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 84
                            },
                            {
                                "Time": "2020-09-09T00:00:00+08:00",
                                "Count": 2,
                                "Usage": 26
                            }
                        ]
                    },
                    {
                        "Specification": "TESHD-10.H264.HD",
                        "Data": [
                            {
                                "Time": "2020-09-07T00:00:00+08:00",
                                "Count": 0,
                                "Usage": 0
                            },
                            {
                                "Time": "2020-09-08T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 84
                            },
                            {
                                "Time": "2020-09-09T00:00:00+08:00",
                                "Count": 0,
                                "Usage": 0
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

