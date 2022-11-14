**Example 1: 提交数据导出任务**



Input: 

```
tccli wedata CommitExportTask --cli-unfold-argument  \
    --RuleExecId 1 \
    --ProjectId 1 \
    --ExportType 1 \
    --QueueName xx \
    --ExecutorGroupId xx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

