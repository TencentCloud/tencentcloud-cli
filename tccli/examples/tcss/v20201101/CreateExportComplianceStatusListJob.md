**Example 1: 创建一个导出安全合规信息的任务**



Input: 

```
tccli tcss CreateExportComplianceStatusListJob --cli-unfold-argument  \
    --AssetType ASSET_CONTAINER \
    --ExportByAsset False \
    --ExportAll False
```

Output: 
```
{
    "Response": {
        "JobId": "e4409223-8e92-45db-a857-11b1ff547c79",
        "RequestId": "3e6756ce-6512-498d-a9fd-8572ef4ce7d3"
    }
}
```

