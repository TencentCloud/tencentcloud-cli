**Example 1: 创建镜像仓库组件关联镜像列表导出任务**



Input: 

```
tccli csip CreateAssetComponentRelatedImageListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 10 \
    --Save 1 \
    --ExportName asset_component
```

Output: 
```
{
    "Response": {
        "JobID": "a80fbb1d-77bf-416d-a076-47875f2fb283",
        "RequestId": "6c6c6d41-0fd0-4749-ba49-b4827725088a"
    }
}
```

