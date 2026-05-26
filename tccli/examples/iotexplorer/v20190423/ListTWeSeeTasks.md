**Example 1: 查询 TWeSee 视觉理解任务列表**



Input: 

```
tccli iotexplorer ListTWeSeeTasks --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceCategory COMPREHENSION \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
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
            }
        ],
        "Total": 1,
        "RequestId": "ecdb8ebc-b257-43f0-af93-105b0cfa94c0"
    }
}
```

**Example 2: 查询 TWeSee 视觉理解任务列表（有时间范围和状态条件）**



Input: 

```
tccli iotexplorer ListTWeSeeTasks --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceCategory COMPREHENSION \
    --Limit 10 \
    --Offset 0 \
    --StartTimeMs 1776621600000 \
    --EndTimeMs 1776636000000 \
    --Status 3
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
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
            }
        ],
        "Total": 1,
        "RequestId": "5e24e488-7948-4ff6-9bd1-76eb3a0cd112"
    }
}
```

