**Example 1: 创建已修复漏洞列表导出任务**



Input: 

```
tccli csip CreateVulFixedExportJob --cli-unfold-argument  \
    --Filters.0.Name Level \
    --Filters.0.Values HIGH CRITICAL
```

Output: 
```
{
    "Response": {
        "JobID": "export-job-12345",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

