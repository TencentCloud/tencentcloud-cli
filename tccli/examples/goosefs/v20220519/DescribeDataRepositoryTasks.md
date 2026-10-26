**Example 1: 列出数据流通任务**

列出数据流通任务

Input: 

```
tccli goosefs DescribeDataRepositoryTasks --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DataRepositoryTaskList": [
            {
                "TaskId": "x_task_123456",
                "TaskName": "mydownload_test",
                "TaskEndTime": "2020-09-22T00:00:00+00:00",
                "TaskCreateTime": "2020-09-22T00:00:00+00:00",
                "Bucket": "mubucket-12500000",
                "TotalCapacity": 104857600,
                "FinishedCapacity": 10,
                "TotalFileNumber": 100,
                "FinishedFileNumber": 30,
                "TaskStatus": "SUCCESS",
                "TaskFailMsg": "",
                "TaskType": "COS_TO_FS",
                "TaskPath": "aaa/bbb",
                "RepositoryType": "MSP_AFM",
                "TextLocation": "http://xx"
            }
        ],
        "TotalCount": 50,
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

