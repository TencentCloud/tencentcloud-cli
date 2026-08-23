**Example 1: 创建镜像仓库列表导出任务**



Input: 

```
tccli csip CreateImageRegistryListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName registry_list
```

Output: 
```
{
    "Response": {
        "JobID": "b6643d91-8fff-4aed-af2e-798df35d85fd",
        "RequestId": "02ec7957-1e1c-41df-bca7-37ad9d9f0e4e"
    }
}
```

