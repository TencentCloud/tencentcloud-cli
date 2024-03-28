**Example 1: 查询规则执行导出结果**



Input: 

```
tccli wedata DescribeRuleExecExportResult --cli-unfold-argument  \
    --ProjectId 456789 \
    --RuleExecId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleExecId": 1,
            "ExportTasks": [
                {
                    "ExportTaskId": 1,
                    "TaskType": 1,
                    "OperatorId": 1,
                    "OperatorName": "zhangsan",
                    "CreateTime": "2023-10-01",
                    "Status": 1,
                    "SchedulerTaskId": "5678979567",
                    "SchedulerCurRunDate": "2023-10-01",
                    "FilePath": "abc",
                    "Expire": 0,
                    "DatasourceName": "hive-79ugihbj",
                    "DbTableName": "test",
                    "RuleName": "规则1",
                    "RuleExecId": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

