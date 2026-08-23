**Example 1: 创建镜像木马病毒列表导出任务**



Input: 

```
tccli csip CreateImageVirusListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName virus_list
```

Output: 
```
{
    "Response": {
        "JobID": "58054077-87e9-46a7-b73b-6a7ff9cddb67",
        "RequestId": "bd413208-7500-42d9-b0ad-154e68f3fda1"
    }
}
```

