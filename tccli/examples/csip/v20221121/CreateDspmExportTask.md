**Example 1: 创建导出任务**



Input: 

```
tccli csip CreateDspmExportTask --cli-unfold-argument  \
    --DangerLevel 0 \
    --DbName cdb-mysql \
    --DbPort 0 \
    --DbIp 127.0.0.1 \
    --AssetsId 3306 \
    --SessionId 1711987200000-140227893131008-2045 \
    --ClientSideIp 127.0.0.1 \
    --EndTime 0 \
    --HitRule 0 \
    --StartTime 0 \
    --FuzzySearch select \
    --UserName root \
    --ClientName VM-0-124 \
    --SourceTypes Agent
```

Output: 
```
{
    "Response": {
        "RequestId": "0e67fb37-ebe9-4e44-8bc8-7810b66ce6a2"
    }
}
```

