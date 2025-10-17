**Example 1: 查询任务是运行记录**

查询任务是运行记录

Input: 

```
tccli wedata DescribeTestRunningRecord --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20250918203021234 \
    --PageSize 10 \
    --PageIndex 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2025-09-18T20:36:21",
                "ErrorMessage": null,
                "ExecutionJobId": "6820250918203615071_2025-09-18T20:36:14+08:00",
                "JobId": 9431,
                "OwnerUin": "100028448903",
                "RecordId": 10823,
                "RecordName": "20250918-2036",
                "Region": "ap-nanjing",
                "ScriptContent": "create database oceanus_test;",
                "StartTime": "2025-09-18T20:36:16",
                "Status": "SUCCESS",
                "SubRecordList": [
                    {
                        "DetailId": 5186,
                        "EndTime": null,
                        "ExecutionJobId": "6820250918203615071_2025-09-18T20:36:14+08:00",
                        "ExecutionSubJobId": "6820250918203615071_0",
                        "HasSubResultSet": true,
                        "LogFilePath": null,
                        "RecordId": 10823,
                        "ResultFilePath": null,
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": null,
                        "ResultTotalCount": 0,
                        "ScriptContent": "create database oceanus_test",
                        "Sequence": "1",
                        "StartTime": "2025-09-18T20:36:16",
                        "Status": "LAUNCHED",
                        "TimeCost": null,
                        "UpdateTime": "2025-09-18T20:36:16"
                    }
                ],
                "TimeCost": 5,
                "UpdateTime": "2025-09-18T20:36:32",
                "UserUin": "100028581064"
            },
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2025-09-18T20:35:41",
                "ErrorMessage": null,
                "ExecutionJobId": "6820250918203532059_2025-09-18T20:35:31+08:00",
                "JobId": 9430,
                "OwnerUin": "100028448903",
                "RecordId": 10822,
                "RecordName": "20250918-2035",
                "Region": "ap-nanjing",
                "ScriptContent": "show databases;",
                "StartTime": "2025-09-18T20:35:34",
                "Status": "SUCCESS",
                "SubRecordList": [
                    {
                        "DetailId": 5185,
                        "EndTime": "2025-09-18T20:35:41",
                        "ExecutionJobId": "6820250918203532059_2025-09-18T20:35:31+08:00",
                        "ExecutionSubJobId": "6820250918203532059_0",
                        "HasSubResultSet": true,
                        "LogFilePath": "xFlowJob/schedule_space/log/1460947878944567296/32/6820250918203532059_0/all.log",
                        "RecordId": 10822,
                        "ResultFilePath": "xFlowJob/schedule_space/result/1460947878944567296/32/6820250918203532059_0/6820250918203532059_0_result.csv",
                        "ResultPreviewCount": 89,
                        "ResultPreviewFilePath": "xFlowJob/schedule_space/result/1460947878944567296/32/6820250918203532059_0/preview_6820250918203532059_0_result.csv",
                        "ResultTotalCount": 89,
                        "ScriptContent": "show databases",
                        "Sequence": "1",
                        "StartTime": "2025-09-18T20:35:36",
                        "Status": "SUCCESS",
                        "TimeCost": 5,
                        "UpdateTime": "2025-09-18T20:35:34"
                    }
                ],
                "TimeCost": 7,
                "UpdateTime": "2025-09-18T20:35:45",
                "UserUin": "100028581064"
            },
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2025-09-18T20:34:25",
                "ErrorMessage": "runner exec engine err",
                "ExecutionJobId": "6820250918203419014_2025-09-18T20:34:18+08:00",
                "JobId": 9429,
                "OwnerUin": "100028448903",
                "RecordId": 10821,
                "RecordName": "20250918-2034",
                "Region": "ap-nanjing",
                "ScriptContent": "show databases;",
                "StartTime": "2025-09-18T20:34:21",
                "Status": "FAILED",
                "SubRecordList": [
                    {
                        "DetailId": 5184,
                        "EndTime": "2025-09-18T20:34:24",
                        "ExecutionJobId": "6820250918203419014_2025-09-18T20:34:18+08:00",
                        "ExecutionSubJobId": "6820250918203419014_0",
                        "HasSubResultSet": true,
                        "LogFilePath": "xFlowJob/schedule_space/log/1460947878944567296/32/6820250918203419014_0/all.log",
                        "RecordId": 10821,
                        "ResultFilePath": "",
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": "",
                        "ResultTotalCount": 0,
                        "ScriptContent": "show databases",
                        "Sequence": "1",
                        "StartTime": "2025-09-18T20:34:22",
                        "Status": "FAILED",
                        "TimeCost": 2,
                        "UpdateTime": "2025-09-18T20:34:20"
                    }
                ],
                "TimeCost": 4,
                "UpdateTime": "2025-09-18T20:34:27",
                "UserUin": "100028581064"
            },
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2025-09-18T20:33:45",
                "ErrorMessage": "runner exec engine err",
                "ExecutionJobId": "6820250918203319040_2025-09-18T20:33:18+08:00",
                "JobId": 9428,
                "OwnerUin": "100028448903",
                "RecordId": 10820,
                "RecordName": "20250918-2033",
                "Region": "ap-nanjing",
                "ScriptContent": "--DLC SQL\n--******************************************************************--\n--author: yukittzhang\n--create time: 2025-09-18 20:30:17\n--******************************************************************--\nshow tables;",
                "StartTime": "2025-09-18T20:33:21",
                "Status": "FAILED",
                "SubRecordList": [
                    {
                        "DetailId": 5183,
                        "EndTime": "2025-09-18T20:33:43",
                        "ExecutionJobId": "6820250918203319040_2025-09-18T20:33:18+08:00",
                        "ExecutionSubJobId": "6820250918203319040_0",
                        "HasSubResultSet": true,
                        "LogFilePath": "xFlowJob/schedule_space/log/1460947878944567296/32/6820250918203319040_0/all.log",
                        "RecordId": 10820,
                        "ResultFilePath": "",
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": "",
                        "ResultTotalCount": 0,
                        "ScriptContent": "show tables",
                        "Sequence": "1",
                        "StartTime": "2025-09-18T20:33:22",
                        "Status": "FAILED",
                        "TimeCost": 21,
                        "UpdateTime": "2025-09-18T20:33:21"
                    }
                ],
                "TimeCost": 24,
                "UpdateTime": "2025-09-18T20:33:47",
                "UserUin": "100028581064"
            },
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2025-09-18T20:31:57",
                "ErrorMessage": "runner exec engine err",
                "ExecutionJobId": "6820250918203151003_2025-09-18T20:31:50+08:00",
                "JobId": 9427,
                "OwnerUin": "100028448903",
                "RecordId": 10819,
                "RecordName": "20250918-2031",
                "Region": "ap-nanjing",
                "ScriptContent": "--DLC SQL\n--******************************************************************--\n--author: yukittzhang\n--create time: 2025-09-18 20:30:17\n--******************************************************************--\nselect 1",
                "StartTime": "2025-09-18T20:31:53",
                "Status": "FAILED",
                "SubRecordList": [
                    {
                        "DetailId": 5182,
                        "EndTime": "2025-09-18T20:31:56",
                        "ExecutionJobId": "6820250918203151003_2025-09-18T20:31:50+08:00",
                        "ExecutionSubJobId": "6820250918203151003_0",
                        "HasSubResultSet": true,
                        "LogFilePath": "xFlowJob/schedule_space/log/1460947878944567296/32/6820250918203151003_0/all.log",
                        "RecordId": 10819,
                        "ResultFilePath": "",
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": "",
                        "ResultTotalCount": 0,
                        "ScriptContent": "select 1",
                        "Sequence": "1",
                        "StartTime": "2025-09-18T20:31:55",
                        "Status": "FAILED",
                        "TimeCost": 1,
                        "UpdateTime": "2025-09-18T20:31:53"
                    }
                ],
                "TimeCost": 4,
                "UpdateTime": "2025-09-18T20:31:59",
                "UserUin": "100028581064"
            }
        ],
        "RequestId": "3c24193f-5cf7-4ca7-af70-10203586ef82",
        "TotalItems": 1,
        "TotalPages": 1
    }
}
```

