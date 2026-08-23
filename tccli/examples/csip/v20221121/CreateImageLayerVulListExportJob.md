**Example 1: 创建镜像层漏洞列表导出任务**



Input: 

```
tccli csip CreateImageLayerVulListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 100 \
    --Save 1 \
    --ExportName vul_list
```

Output: 
```
{
    "Response": {
        "JobID": "db1857b1-8dcd-47e8-9ab3-6a762064bbdf",
        "RequestId": "b3a8fcf3-2bf2-4f1d-a3a1-8c2ddeffbb6e"
    }
}
```

