**Example 1: 创建动态资产导出任务**



Input: 

```
tccli csip CreateDynamicAssetsExportJob --cli-unfold-argument  \
    --Provider tencent \
    --AssetType cvm_instance \
    --MemberId mem*0acb***2*9*4daee \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc
```

Output: 
```
{
    "Response": {
        "JobId": "f04e2c67-c096-47dc-969c-33782cb7702d",
        "RequestId": "4baecf28-bec4-4c62-b9ca-c15c414c1e09"
    }
}
```

