**Example 1: 创建风险中心扫描任务**

创建风险中心扫描任务

Input: 

```
tccli csip CreateRiskCenterScanTask --cli-unfold-argument  \
    --TaskName abc \
    --Assets.0.AssetName abc \
    --Assets.0.InstanceType abc \
    --Assets.0.AssetType abc \
    --Assets.0.Asset abc \
    --Assets.0.Region abc \
    --ScanAssetType 0 \
    --ScanItem abc \
    --ScanPlanType 0 \
    --ScanPlanContent abc \
    --SelfDefiningAssets abc \
    --TaskMode 0
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

