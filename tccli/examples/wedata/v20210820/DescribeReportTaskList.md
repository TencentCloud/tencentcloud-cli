**Example 1: 正常调用**

正常调用

Input: 

```
tccli wedata DescribeReportTaskList --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10 \
    --EngineTaskId 4dfedddfcc1611efa2b9525400942df5
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNum": 1,
            "PageSize": 10,
            "Rows": [
                {
                    "AppID": "1315051789",
                    "EngineExeEndTime": "2025-01-06 18:09:25",
                    "EngineExeStartTime": "2025-01-06 18:09:24",
                    "EngineExeStatus": "SUCCESS",
                    "EngineExeUser": null,
                    "EngineName": "DLC_Standard_Presto",
                    "EngineSubType": "DLC_Standard_Presto",
                    "EngineTaskId": "4dfedddfcc1611efa2b9525400942df5",
                    "EngineType": "DLC",
                    "InChargeId": null,
                    "InstanceId": "ffda85b9-5258-477c-a965-380b3d4d3f64",
                    "JobId": "a93d192c-96f0-487e-9a81-7e7b964d22ef",
                    "OnwerUid": null,
                    "ProductSource": "DATA_EXPLORATION",
                    "ProjectId": "1460947878944567296",
                    "TaskId": null,
                    "TaskName": null,
                    "TaskTypeId": null
                }
            ],
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "cf410329-1b40-46cb-91ea-8d6d970c819b"
    }
}
```

