**Example 1: 成功调用**



Input: 

```
tccli wedata DescribeReportTaskDetail --cli-unfold-argument  \
    --EngineTaskId fd04099ecc1611ef9abe525400eda0b2
```

Output: 
```
{
    "Response": {
        "Data": {
            "BusinessInfo": null,
            "EngineExeEndTime": "0002-11-30 00:00:00",
            "EngineExeStartTime": "2025-04-01 14:16:12",
            "EngineExeStatus": "RUNNING",
            "EngineTaskId": "hadoop_20250401141612_67b7d4fc-579e-4287-b385-e1f63b68c6ce",
            "EngineTaskInfo": {
                "ApplicationId": "application_1682679126503_154551",
                "CmdArgs": null,
                "CuConsume": null,
                "EmrUserName": "hadoop",
                "EngineExeStatus": null,
                "EngineExeTime": "0002-11-30 00:00:00",
                "EngineExeTimeCost": 6,
                "EngineName": "emr-k3s4qsys",
                "EngineSubmitTime": "2025-04-01 14:16:12",
                "InputBytesSum": null,
                "MemorySeconds": 34193,
                "OutputBytesSum": null,
                "OutputFilesNum": null,
                "OutputRecordsSum": null,
                "OutputSmallFilesNum": null,
                "QueryId": "hadoop_20250401141612_67b7d4fc-579e-4287-b385-e1f63b68c6ce",
                "QueryResultTime": null,
                "ResourceUsage": null,
                "ShuffleReadBytesSum": null,
                "ShuffleReadRecordsSum": null,
                "TaskContent": "select concat(total_num,&#039;,&#039;, &#039;&#039;), total_num from (select count(*) as total_num from default.person_hour_1 where 1 = 1)tbl",
                "TaskKind": null,
                "TaskType": "tez",
                "VCoreSeconds": 19,
                "WaitTime": null
            },
            "TaskTypeId": 34
        },
        "RequestId": "7d24e998-058b-4ef4-b9bd-70fce1bb4a2e"
    }
}
```

