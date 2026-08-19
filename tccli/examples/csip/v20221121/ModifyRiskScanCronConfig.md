**Example 1: 更新用户周期检测计划**



Input: 

```
tccli csip ModifyRiskScanCronConfig --cli-unfold-argument  \
    --CronStatus 1 \
    --CronPlanContent 0 0 17 * * 1,2,3,4,5,6,7 * \
    --RuleAutoEnable True \
    --ScanPlanTimezone Asia/Shanghai \
    --IncrementAssetScanRisk True
```

Output: 
```
{
    "Response": {
        "Message": "Success",
        "RequestId": "649d1104-32de-4165-b3a1-13bb55307128"
    }
}
```

