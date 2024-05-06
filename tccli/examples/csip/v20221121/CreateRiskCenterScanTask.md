**Example 1: 创建风险中心扫描任务**

创建风险中心扫描任务

Input: 

```
tccli csip CreateRiskCenterScanTask --cli-unfold-argument  \
    --MemberId abc \
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
    --ScanFrom abc \
    --TaskAdvanceCFG.PortRisk.0.PortSets abc \
    --TaskAdvanceCFG.PortRisk.0.CheckType 0 \
    --TaskAdvanceCFG.PortRisk.0.Detail abc \
    --TaskAdvanceCFG.PortRisk.0.Enable 0 \
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

