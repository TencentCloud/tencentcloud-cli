**Example 1: 实时任务同步速度趋势**

实时任务同步速度趋势

Input: 

```
tccli wedata DescribeRealTimeTaskSpeed --cli-unfold-argument  \
    --TaskId task33 \
    --StartTime 1712803796000 \
    --EndTime 1712803996000 \
    --Granularity 1213 \
    --ProjectId 1486804694126882816
```

Output: 
```
{
    "Response": {
        "RecordsSpeedList": [
            {
                "NodeType": "INPUT",
                "NodeName": "1",
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
                "NodeType": "INPUT",
                "NodeName": "1",
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
                    "NodeType": "INPUT",
                    "NodeName": "1",
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
                    "NodeType": "INPUT",
                    "NodeName": "1"
                }
            ]
        },
        "RequestId": "977662"
    }
}
```

