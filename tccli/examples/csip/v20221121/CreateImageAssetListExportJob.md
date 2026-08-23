**Example 1: 创建镜像资产列表导出任务**



Input: 

```
tccli csip CreateImageAssetListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName asset_list
```

Output: 
```
{
    "Response": {
        "JobID": "8a487ee1-f811-40a1-91f8-53cd45c408c7",
        "RequestId": "67baed5c-a947-47e9-b5f7-4259e6f8de0e"
    }
}
```

