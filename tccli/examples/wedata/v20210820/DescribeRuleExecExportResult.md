**Example 1: 查询规则执行导出结果**



Input: 

```
tccli wedata DescribeRuleExecExportResult --cli-unfold-argument  \
    --RuleExecId 1 \
    --ProjectId xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleExecId": 1,
            "ExportTasks": [
                {
                    "Status": 1,
                    "SchedulerCurRunDate": "xx",
                    "OperatorId": 1,
                    "FilePath": "xx",
                    "ExportTaskId": 1,
                    "CreateTime": "xx",
                    "TaskType": 1,
                    "SchedulerTaskId": "xx",
                    "OperatorName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

