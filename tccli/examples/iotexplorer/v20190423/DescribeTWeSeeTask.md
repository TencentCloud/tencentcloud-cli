**Example 1: 查询 TWeSee 视觉理解任务详情**



Input: 

```
tccli iotexplorer DescribeTWeSeeTask --cli-unfold-argument  \
    --TaskId comp-d57939bb-b155-5623-c7e7-1fb8dd0654dd
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
            "ComprehensionResult": {
                "AlternativeSummary": "A person in white pants and a white shirt walks on a wet sidewalk.",
                "DetectedClassifications": [
                    "person"
                ],
                "Summary": "穿白色衣裤的人在湿滑的人行道上行走"
            },
            "CostAdvanced": 0,
            "CostBasic": 2,
            "CreateTime": 1776629116,
            "Files": [],
            "FilesInfo": [],
            "Metadata": {
                "ChannelId": 0,
                "CustomId": "_sys_id1_data",
                "DeviceName": "dev002",
                "EndTimeMs": 1776629110000,
                "ProductId": "4AHMY9X89Y",
                "StartTimeMs": 1776629102000
            },
            "ServiceCategory": "COMPREHENSION",
            "ServiceTier": "BASIC",
            "ServiceType": "VID_COMP",
            "Status": 3,
            "TaskId": "comp-d57939bb-b155-5623-c7e7-1fb8dd0654dd",
            "UpdateTime": 1776629119
        },
        "RequestId": "1d84d34c-ad3d-44bc-86f0-cf62340d5e56"
    }
}
```

