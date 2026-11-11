**Example 1: 导出资产基线风险**

导出资产基线风险

Input: 

```
tccli csip CreateAssetBaselineRiskExportJob --cli-unfold-argument  \
    --AssetUniqueID 87cd7655-**********9ea1-6267cb76707d \
    --AssetType HOST \
    --AssetAppID 260000096 \
    --Name 资产导出 \
    --MemberId mem-****e**-*******52f66e429
```

Output: 
```
{
    "Response": {
        "JobId": "d1cbc89d-ee9c-46d7-8a86-fa8c418f8719",
        "RequestId": "cabf5bae-f0ac-4e69-b663-cd0bb5b6fcf6"
    }
}
```

