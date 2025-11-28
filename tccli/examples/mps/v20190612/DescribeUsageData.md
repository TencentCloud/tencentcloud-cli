**Example 1: 查询媒体处理用量**

查询用量

Input: 

```
tccli mps DescribeUsageData --cli-unfold-argument  \
    --EndTime 2019-07-03T00:00:00+08:00 \
    --StartTime 2019-07-02T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskType": "Transcode",
                "Summary": [
                    {
                        "Time": "2019-07-02T00:00:00+08:00",
                        "Count": 22,
                        "Usage": 2200
                    },
                    {
                        "Time": "2019-07-03T00:00:00+08:00",
                        "Count": 22,
                        "Usage": 2200
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
                        "Specification": "Standard.H265.4K",
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

