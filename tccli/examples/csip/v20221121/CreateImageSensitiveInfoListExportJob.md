**Example 1: 创建镜像敏感信息列表导出任务**



Input: 

```
tccli csip CreateImageSensitiveInfoListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName info_list
```

Output: 
```
{
    "Response": {
        "JobID": "b9f8665d-bc76-4308-93fe-9096012c3c5e",
        "RequestId": "2a204d72-0110-4c44-b837-a890e559f11d"
    }
}
```

