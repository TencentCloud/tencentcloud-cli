**Example 1: 更新规则组执行策略**



Input: 

```
tccli wedata ModifyExecStrategy --cli-unfold-argument  \
    --DatabaseId xx \
    --Tasks.0.TaskName xx \
    --Tasks.0.WorkflowId xx \
    --Tasks.0.TaskId xx \
    --DelayTime 1 \
    --ExecQueue xx \
    --RuleGroupId 1 \
    --ProjectId xx \
    --ExecutorGroupName xx \
    --TaskAction xx \
    --CycleType xx \
    --TableId xx \
    --StartTime xx \
    --MonitorType 1 \
    --EndTime xx \
    --ExecutorGroupId xx \
    --CycleStep 1 \
    --DatasourceId xx
```

Output: 
```
{
    "Response": {
        "Data": 123456,
        "RequestId": "xx"
    }
}
```

