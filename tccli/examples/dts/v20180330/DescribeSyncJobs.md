**Example 1: 查询灾备同步任务**



Input: 

```
tccli dts DescribeSyncJobs --cli-unfold-argument  \
    --Order CreateTime \
    --OrderSeq DESC \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "JobList": [
            {
                "JobId": "sync-blj8wnt1",
                "JobName": "okJobName1",
                "SyncOption": {
                    "SyncObject": 1,
                    "RunMode": 1,
                    "SyncType": 3,
                    "ConsistencyType": 1
                },
                "SrcAccessType": "cdb",
                "SrcDatabaseType": "mysql",
                "SrcInfo": {
                    "InstanceId": "cdb-e28hhsjt",
                    "Region": "ap-shanghai"
                },
                "DstAccessType": "cdb",
                "DstDatabaseType": "mysql",
                "DstInfo": {
                    "InstanceId": "cdb-mdgezf4d",
                    "Region": "ap-shanghai"
                },
                "Detail": {
                    "StepAll": 0,
                    "StepNow": 0,
                    "Progress": "0",
                    "CurrentStepProgress": "",
                    "MasterSlaveDistance": 0,
                    "SecondsBehindMaster": 0,
                    "StepInfo": []
                },
                "Status": 4,
                "DatabaseInfo": "Array",
                "CreateTime": "2018-06-22 21:59:16",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00"
            },
            {
                "JobId": "sync-2hoficf5",
                "JobName": "test_create_sync_jobName_0622_2100",
                "SyncOption": {
                    "SyncObject": 2,
                    "RunMode": 1,
                    "SyncType": 3,
                    "ConsistencyType": 1
                },
                "SrcAccessType": "cdb",
                "SrcDatabaseType": "mysql",
                "SrcInfo": {
                    "InstanceId": "cdb-6ygku747",
                    "Region": "ap-guangzhou"
                },
                "DstAccessType": "cdb",
                "DstDatabaseType": "mysql",
                "DstInfo": {
                    "InstanceId": "cdb-ddlroj4d",
                    "Region": "ap-shanghai"
                },
                "Detail": {
                    "StepAll": 0,
                    "StepNow": 0,
                    "Progress": "",
                    "CurrentStepProgress": "",
                    "MasterSlaveDistance": 0,
                    "SecondsBehindMaster": 0,
                    "StepInfo": []
                },
                "Status": 1,
                "DatabaseInfo": "Array",
                "CreateTime": "2018-06-22 20:37:28",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "1ae80092-45be-4cf2-b313-026b6380463e"
    }
}
```

