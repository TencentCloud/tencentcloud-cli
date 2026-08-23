**Example 1: 创建镜像漏洞概览列表导出任务**



Input: 

```
tccli csip CreateImageVulSummaryListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName summary_list
```

Output: 
```
{
    "Response": {
        "JobID": "6bbbc6fe-1b9f-466f-be68-9a55fc591f69",
        "RequestId": "5cf47934-8d9b-4287-9e4d-2ae60f221429"
    }
}
```

