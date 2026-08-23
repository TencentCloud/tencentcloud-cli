**Example 1: 创建镜像关联主机资产列表导出任务**



Input: 

```
tccli csip CreateImageAssociatedHostListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 10 \
    --Save 1 \
    --ExportName host_list
```

Output: 
```
{
    "Response": {
        "JobID": "5de4e9a0-f935-4258-b070-267d99e65230",
        "RequestId": "25680a74-aea7-483e-89d8-4ccc3520065f"
    }
}
```

