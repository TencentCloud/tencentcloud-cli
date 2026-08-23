**Example 1: 创建镜像漏洞列表导出任务**



Input: 

```
tccli csip CreateImageVulListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName vul_list
```

Output: 
```
{
    "Response": {
        "JobID": "0c179c7d-81b2-44b8-b70f-44d73df46ef4",
        "RequestId": "072d69f1-1d69-41a5-a137-d981bbf6fa50"
    }
}
```

