**Example 1: 获取迁移任务列表**

获取迁移任务列表

Input: 

```
tccli msp ListMigrationTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 13,
        "Tasks": [
            {
                "TaskId": "msp-81pzxxx",
                "TaskName": "xxx",
                "MigrationType": "file",
                "Status": "migrating",
                "ProjectId": 0,
                "ProjectName": "",
                "SrcInfo": {
                    "Ip": "127.0.0.1",
                    "Port": "80",
                    "Region": "cos.ap-beijing",
                    "InstanceId": "-"
                },
                "DstInfo": {
                    "Ip": "127.0.0.1",
                    "Port": "80",
                    "Region": "127.0.0.1",
                    "InstanceId": "-"
                },
                "MigrationTimeLine": {
                    "CreateTime": "2018-07-13 15:00:00",
                    "EndTime": "-"
                },
                "Updated": "2018-07-13 15:00:00"
            },
            {
                "TaskId": "msp-j33xxx",
                "TaskName": "ccc",
                "MigrationType": "database",
                "Status": "migrating",
                "ProjectId": 0,
                "ProjectName": "",
                "SrcInfo": {
                    "Ip": "127.0.0.1",
                    "Port": "80",
                    "Region": "ap-beijing",
                    "InstanceId": "-"
                },
                "DstInfo": {
                    "Ip": "127.0.0.1",
                    "Port": "80",
                    "Region": "ap-beijing",
                    "InstanceId": "-"
                },
                "MigrationTimeLine": {
                    "CreateTime": "2018-07-13 15:00:00",
                    "EndTime": "-"
                },
                "Updated": "2018-07-13 15:00:00"
            }
        ],
        "RequestId": "b7534e17-4744-4787-95a9-05f7f0419f4c"
    }
}
```

