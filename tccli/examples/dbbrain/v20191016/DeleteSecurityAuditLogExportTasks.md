**Example 1: 删除安全审计日志导出任务**

删除安全审计日志导出任务。

Input: 

```
tccli dbbrain DeleteSecurityAuditLogExportTasks --cli-unfold-argument  \
    --SecAuditGroupId sag-01z37k3f \
    --AsyncRequestIds 1 \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "5fdab910-5c9e-11eb-a610-8717ee1b1000"
    }
}
```

