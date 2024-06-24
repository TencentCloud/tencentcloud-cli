**Example 1: 查询引擎规格详情**



Input: 

```
tccli dlc DescribeDataEnginesScaleDetail --cli-unfold-argument  \
    --StartTime 2024-06-06 12:00:00 \
    --EndTime 2024-06-06 13:00:00 \
    --DataEngineNames dataengine-abc
```

Output: 
```
{
    "Response": {
        "Scales": [
            {
                "DataEngineId": "abc",
                "DataEngineName": "abc",
                "ScaleDetail": [
                    {
                        "StartTime": "abc",
                        "EndTime": "abc",
                        "CU": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

