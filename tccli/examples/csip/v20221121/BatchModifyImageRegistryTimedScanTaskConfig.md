**Example 1: 批量修改镜像仓库定时扫描任务配置**



Input: 

```
tccli csip BatchModifyImageRegistryTimedScanTaskConfig --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 5 \
    --Enable False \
    --ScanType VUL \
    --Schedule.CycleType DAILY \
    --Schedule.CycleDays 2 \
    --Schedule.StartTime 12:00 \
    --Schedule.Timezone Asia/Shanghai \
    --Timeout 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "96918abb-84c4-4eba-ba93-9cce36777935"
    }
}
```

