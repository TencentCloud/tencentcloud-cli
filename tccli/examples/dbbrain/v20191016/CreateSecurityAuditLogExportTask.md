**Example 1: 创建安全审计日志导出任务**



Input: 

```
tccli dbbrain CreateSecurityAuditLogExportTask --cli-unfold-argument  \
    --SecAuditGroupId sag-01z37k3f \
    --Product mysql \
    --StartTime 2019-01-01T00:00:00+00:00 \
    --EndTime 2019-01-02T00:00:00+00:00 \
    --DangerLevels 1 2 3
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": 1,
        "RequestId": "0c4959d0-5abb-11eb-862f-653dd83af000"
    }
}
```

