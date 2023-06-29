**Example 1: 创建一个导出安全合规信息的任务**



Input: 

```
tccli tcss CreateExportComplianceStatusListJob --cli-unfold-argument  \
    --AssetType ASSET_CONTAINER \
    --ExportByAsset False \
    --ExportAll True
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "JobId": "xxxx"
    }
}
```

