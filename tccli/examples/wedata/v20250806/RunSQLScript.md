**Example 1: 成功响应**



Input: 

```
tccli wedata RunSQLScript --cli-unfold-argument  \
    --ScriptId 971c1520-836f-41be-b13f-7a6c637317c8 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2025-09-18 15:28:32",
            "EndTime": "2025-09-18 15:28:42",
            "JobExecutionList": null,
            "JobId": "6820250918152834057",
            "JobName": "SQL脚本执行任务",
            "JobType": "EXECUTOR",
            "OwnerUin": "100043952936",
            "ScriptContent": "--******************************************************************--\n--author: gordonzzhu\n--create time: 2025-01-14 21:05:48\n--可在左侧【库表】中查看数据库表信息\n--可在右上角修改数据探索的执行数据源等信息。\n--******************************************************************--\nSELECT 1;",
            "ScriptContentTruncate": false,
            "ScriptId": "0f2777fa-46d7-42cd-8b59-74ce47a375c0",
            "Status": "S",
            "TimeCost": 10000,
            "UpdateTime": "2025-09-18 15:28:42",
            "UserUin": "100028448903"
        },
        "RequestId": "08955a5f-497f-4bac-bac6-99c75191ffa7"
    }
}
```

