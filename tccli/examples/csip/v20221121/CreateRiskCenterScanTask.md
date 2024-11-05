**Example 1: 创建风险中心扫描任务**

创建风险中心扫描任务

Input: 

```
tccli csip CreateRiskCenterScanTask --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --TaskName scan-task \
    --Assets.0.AssetName insname \
    --Assets.0.InstanceType CVM \
    --Assets.0.AssetType Instance \
    --Assets.0.Asset ns-mx19k34r \
    --Assets.0.Region ap-guangzhou \
    --ScanAssetType 1 \
    --ScanItem port \
    --ScanPlanType 2 \
    --ScanPlanContent 38 53 11 */1 * * * \
    --ScanFrom csip \
    --TaskAdvanceCFG.PortRisk.0.PortSets 80 \
    --TaskAdvanceCFG.PortRisk.0.CheckType 0 \
    --TaskAdvanceCFG.PortRisk.0.Detail port info \
    --TaskAdvanceCFG.PortRisk.0.Enable 0 \
    --TaskMode 0
```

Output: 
```
{
    "Response": {
        "TaskId": "rmis-18yeflff",
        "RequestId": "7cf2ba3d-87ad-4691-a374-fd92ec11d9c8"
    }
}
```

