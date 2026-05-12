**Example 1: 修改Dspm安全分析开关**



Input: 

```
tccli csip ModifyDspmAssetSecurityAnalysisSwitch --cli-unfold-argument  \
    --Instances.0.AssetId cdb-mmg7t7v0 \
    --Instances.0.AssetType cdb \
    --Instances.0.Region ap-guangzhou \
    --Instances.0.AppId 260083796 \
    --MemberId mem-6wfo0fzks3 \
    --Enable 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0d5d0327-41a1-46d3-95cc-55916dcd4f97"
    }
}
```

