**Example 1: 查询引擎规格详情**



Input: 

```
tccli dlc DescribeDataEnginesScaleDetail --cli-unfold-argument  \
    --StartTime 2024-06-06 12:00:00 \
    --EndTime 2024-06-06 13:00:00 \
    --DataEngineNames dataengine-presto
```

Output: 
```
{
    "Response": {
        "RequestId": "7348577b-a168-467b-bd68-3c396b78b608",
        "Scales": [
            {
                "DataEngineId": "DataEngine-2ctxxxj3",
                "DataEngineName": "dataengine-presto",
                "ScaleDetail": [
                    {
                        "StartTime": "2025-01-14 14:55:00",
                        "EndTime": "2025-01-14 14:59:01",
                        "CU": 0
                    },
                    {
                        "StartTime": "2025-01-14 14:59:01",
                        "EndTime": "2025-01-14 15:12:03",
                        "CU": 128
                    },
                    {
                        "StartTime": "2025-01-14 15:12:03",
                        "EndTime": "2025-01-14 15:19:04",
                        "CU": 0
                    },
                    {
                        "StartTime": "2025-01-14 15:19:04",
                        "EndTime": "2025-01-14 15:35:07",
                        "CU": 128
                    },
                    {
                        "StartTime": "2025-01-14 15:36:00",
                        "EndTime": "2025-01-14 15:36:00",
                        "CU": 128
                    }
                ]
            }
        ]
    }
}
```

