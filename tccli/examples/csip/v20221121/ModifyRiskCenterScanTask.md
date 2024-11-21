**Example 1: 修改风险中心扫描任务**

修改风险中心扫描任务

Input: 

```
tccli csip ModifyRiskCenterScanTask --cli-unfold-argument  \
    --MemberId mem-fe191feeedcc2567 \
    --TaskName asset scan task \
    --Assets.0.AssetName cvm-t1 \
    --Assets.0.InstanceType CVM \
    --Assets.0.AssetType Instance \
    --Assets.0.Asset ins-mx19k3r4 \
    --Assets.0.Region guangzhou \
    --ScanAssetType 0 \
    --ScanItem port \
    --ScanPlanType 0 \
    --ScanPlanContent 38 53 11 */1 * * * \
    --SelfDefiningAssets 120.53.53.53 \
    --TaskId rmis-112hq236 \
    --TaskAdvanceCFG.PortRisk.0.PortSets 80 \
    --TaskAdvanceCFG.PortRisk.0.CheckType 0 \
    --TaskAdvanceCFG.PortRisk.0.Detail port info \
    --TaskAdvanceCFG.PortRisk.0.Enable 0 \
    --TaskAdvanceCFG.VulRisk.0.RiskId fc41d3fb24eb96a6dfb12c68e20ebf4b \
    --TaskAdvanceCFG.VulRisk.0.Enable 0 \
    --TaskAdvanceCFG.WeakPwdRisk.0.CheckItemId 151 \
    --TaskAdvanceCFG.WeakPwdRisk.0.Enable 0 \
    --TaskAdvanceCFG.CFGRisk.0.ItemId 161 \
    --TaskAdvanceCFG.CFGRisk.0.Enable 0 \
    --TaskAdvanceCFG.CFGRisk.0.ResourceType CentOS7 \
    --TaskMode 0
```

Output: 
```
{
    "Response": {
        "TaskId": "rmis-112hq236",
        "Status": 0,
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```

