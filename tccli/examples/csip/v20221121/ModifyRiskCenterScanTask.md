**Example 1: 修改风险中心扫描任务**

修改风险中心扫描任务

Input: 

```
tccli csip ModifyRiskCenterScanTask --cli-unfold-argument  \
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
    --TaskId abc \
    --TaskAdvanceCFG.PortRisk.0.PortSets abc \
    --TaskAdvanceCFG.PortRisk.0.CheckType 0 \
    --TaskAdvanceCFG.PortRisk.0.Detail abc \
    --TaskAdvanceCFG.PortRisk.0.Enable 0 \
    --TaskAdvanceCFG.VulRisk.0.RiskId abc \
    --TaskAdvanceCFG.VulRisk.0.Enable 0 \
    --TaskAdvanceCFG.WeakPwdRisk.0.CheckItemId 0 \
    --TaskAdvanceCFG.WeakPwdRisk.0.Enable 0 \
    --TaskAdvanceCFG.CFGRisk.0.ItemId abc \
    --TaskAdvanceCFG.CFGRisk.0.Enable 0 \
    --TaskAdvanceCFG.CFGRisk.0.ResourceType abc \
    --TaskMode 0
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "Status": 0,
        "RequestId": "abc"
    }
}
```

