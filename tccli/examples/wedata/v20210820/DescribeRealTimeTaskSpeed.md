**Example 1: 实时任务同步速度趋势**

实时任务同步速度趋势

Input: 

```
tccli wedata DescribeRealTimeTaskSpeed --cli-unfold-argument  \
    --ProjectId xx \
    --EndTime 1 \
    --StartTime 1 \
    --TaskId xx \
    --Granularity 1
```

Output: 
```
{
    "Response": {
        "BytesSpeedList": [
            {
                "Values": [
                    {
                        "Speed": 0.0,
                        "Time": 1
                    }
                ],
                "NodeType": "xx",
                "NodeName": "xx"
            }
        ],
        "RecordsSpeedList": [
            {
                "Values": [
                    {
                        "Speed": 0.0,
                        "Time": 1
                    }
                ],
                "NodeType": "xx",
                "NodeName": "xx"
            }
        ],
        "Data": {
            "BytesSpeedList": [
                {
                    "Values": [
                        {
                            "Speed": 0.0,
                            "Time": 1
                        }
                    ],
                    "NodeType": "xx",
                    "NodeName": "xx"
                }
            ],
            "RecordsSpeedList": [
                {
                    "NodeType": "xx",
                    "NodeName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

