**Example 1: 修改镜像仓库定时扫描任务配置**



Input: 

```
tccli csip ModifyImageRegistryTimedScanTaskConfig --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 3 \
    --Name 定时扫描任务7 \
    --Enable False \
    --ScanType VUL \
    --Schedule.CycleType DAILY \
    --Schedule.CycleDays 1 \
    --Schedule.StartTime 16:00 \
    --Schedule.Timezone Asia/Shanghai \
    --Target.Mode MANUAL \
    --Target.ExcludeImages 518 \
    --Target.Images 573 \
    --Target.AutoMatch.Clusters 1 \
    --Filter.RegistryType ccr \
    --Filter.Namespace openclaw \
    --Timeout 1800
```

Output: 
```
{
    "Response": {
        "RequestId": "ceb5ef9d-f276-4406-b5fc-b0f95083ea6f"
    }
}
```

