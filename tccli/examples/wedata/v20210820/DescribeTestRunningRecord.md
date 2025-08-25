**Example 1: 试运行记录列表**

试运行记录列表

Input: 

```
tccli wedata DescribeTestRunningRecord --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20240910145214240 \
    --SearchUserUin 100028578763 \
    --CreateTime 2024-10-22 00:00:00 \
    --EndTime 2024-10-29 23:59:59
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2024-10-28T10:21:50",
                "ExecutionJobId": "6820241028102142451_2024-10-28T10:21:40+08:00",
                "JobId": 5531,
                "OwnerUin": "100028448903",
                "RecordId": 5407,
                "RecordName": "20241028-1021",
                "Region": "ap-nanjing",
                "ScriptContent": "--Hive SQL\n--******************************************************************--\n--author: leoftzhang\n--create time: 2024-09-10 14:52:14\n--******************************************************************--\nselect 1;",
                "StartTime": "2024-10-28T10:21:48",
                "Status": "SUCCESS",
                "SubRecordList": [
                    {
                        "DetailId": 324,
                        "EndTime": "2024-10-28T10:21:50",
                        "ExecutionJobId": "6820241028102142451_2024-10-28T10:21:40+08:00",
                        "ExecutionSubJobId": "6820241028102142451",
                        "HasSubResultSet": false,
                        "LogFilePath": "",
                        "RecordId": 5407,
                        "ResultFilePath": "",
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": "",
                        "ResultTotalCount": 0,
                        "ScriptContent": "\n\n\n\n\nselect 1;",
                        "Sequence": "1",
                        "StartTime": "2024-10-28T10:21:48",
                        "Status": "SUCCESS",
                        "TimeCost": 2,
                        "UpdateTime": "2024-10-28T10:21:43"
                    }
                ],
                "TimeCost": 2,
                "UpdateTime": "2024-10-28T10:21:58",
                "UserUin": "100028578763"
            },
            {
                "BucketName": "wedata-fusion-dev-1257305158",
                "EndTime": "2024-10-23T18:11:19",
                "ExecutionJobId": "6820241023181111769_2024-10-23T18:11:09+08:00",
                "JobId": 5469,
                "OwnerUin": "100028448903",
                "RecordId": 5344,
                "RecordName": "20241023-1811",
                "Region": "ap-nanjing",
                "ScriptContent": "--Hive SQL\n--******************************************************************--\n--author: leoftzhang\n--create time: 2024-09-10 14:52:14\n--******************************************************************--\nselect 1;",
                "StartTime": "2024-10-23T18:11:17",
                "Status": "SUCCESS",
                "SubRecordList": [
                    {
                        "DetailId": 323,
                        "EndTime": "2024-10-23T18:11:19",
                        "ExecutionJobId": "6820241023181111769_2024-10-23T18:11:09+08:00",
                        "ExecutionSubJobId": "6820241023181111769",
                        "HasSubResultSet": false,
                        "LogFilePath": "",
                        "RecordId": 5344,
                        "ResultFilePath": "",
                        "ResultPreviewCount": 0,
                        "ResultPreviewFilePath": "",
                        "ResultTotalCount": 0,
                        "ScriptContent": "\n\n\n\n\nselect 1;",
                        "Sequence": "1",
                        "StartTime": "2024-10-23T18:11:17",
                        "Status": "SUCCESS",
                        "TimeCost": 2,
                        "UpdateTime": "2024-10-23T18:11:12"
                    }
                ],
                "TimeCost": 2,
                "UpdateTime": "2024-10-23T18:11:25",
                "UserUin": "100028578763"
            },
            {
                "BucketName": null,
                "EndTime": null,
                "ExecutionJobId": null,
                "JobId": 5459,
                "OwnerUin": "100028448903",
                "RecordId": 5334,
                "RecordName": "20241023-1616",
                "Region": null,
                "ScriptContent": "--Hive SQL\n--******************************************************************--\n--author: leoftzhang\n--create time: 2024-09-10 14:52:14\n--******************************************************************--\nselect 1;",
                "StartTime": null,
                "Status": "FAILED",
                "SubRecordList": null,
                "TimeCost": null,
                "UpdateTime": "2024-10-23T16:16:21",
                "UserUin": "100028578763"
            }
        ],
        "RequestId": "b59164ee-8365-4e8b-a686-f67c30b8c29e"
    }
}
```

