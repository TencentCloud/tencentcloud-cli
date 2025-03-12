**Example 1: 成功调用**

成功调用

Input: 

```
tccli wedata DescribeReportTaskDetail --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10 \
    --EngineTaskId fd04099ecc1611ef9abe525400eda0b2
```

Output: 
```
{
    "Response": {
        "Data": {
            "BusinessInfo": null,
            "EngineExeEndTime": "2025-01-06 18:14:18",
            "EngineExeStartTime": "2025-01-06 18:14:17",
            "EngineExeStatus": null,
            "EngineTaskId": "fd04099ecc1611ef9abe525400eda0b2",
            "EngineTaskInfo": {
                "CmdArgs": "",
                "CuConsume": null,
                "EngineExeStatus": null,
                "EngineExeTime": null,
                "EngineExeTimes": null,
                "EngineName": "DLC_Standard_Presto",
                "EngineSubmitTime": null,
                "InputBytesSum": null,
                "OutputBytesSum": null,
                "OutputFilesNum": null,
                "OutputRecordsSum": null,
                "OutputSmallFilesNum": null,
                "QueryResultTime": null,
                "ResourceUsage": -1,
                "ShuffleReadBytesSum": null,
                "ShuffleReadRecordsSum": null,
                "TaskContent": "SELECT  id\nFROM    \"DataLakeCatalog\".\"a0a0a\".\"kuantest1\"\nlimit   10",
                "TaskKind": "KyuubiSQLTask",
                "TaskType": "StandardPrestoSQLTask",
                "WaitTime": null
            },
            "TaskTypeId": null
        },
        "RequestId": "92c0c30f-286f-4a8c-a167-a5f22df82ae8"
    }
}
```

