**Example 1: 提交数据导出任务**



Input: 

```
tccli wedata CommitExportTask --cli-unfold-argument  \
    --ProjectId 67898 \
    --RuleExecId 1 \
    --ExportType 1 \
    --ExecutorGroupId 56776578 \
    --QueueName test
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

