**Example 1: 实时任务同步速度趋势**

实时任务同步速度趋势

Input: 

```
tccli wedata DescribeRealTimeTaskSpeed --cli-unfold-argument  \
    --TaskId abc \
    --StartTime 1 \
    --EndTime 1 \
    --Granularity 1 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "RecordsSpeedList": [
            {
                "NodeType": "abc",
                "NodeName": "abc",
                "Values": [
                    {
                        "Time": 1,
                        "Speed": 0
                    }
                ]
            }
        ],
        "BytesSpeedList": [
            {
                "NodeType": "abc",
                "NodeName": "abc",
                "Values": [
                    {
                        "Time": 1,
                        "Speed": 0
                    }
                ]
            }
        ],
        "Data": {
            "RecordsSpeedList": [
                {
                    "NodeType": "abc",
                    "NodeName": "abc",
                    "Values": [
                        {
                            "Time": 1,
                            "Speed": 0
                        }
                    ]
                }
            ],
            "BytesSpeedList": [
                {
                    "Values": [
                        {
                            "Speed": 0,
                            "Time": 1
                        }
                    ],
                    "NodeType": "abc",
                    "NodeName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

