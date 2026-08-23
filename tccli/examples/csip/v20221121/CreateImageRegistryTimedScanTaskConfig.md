**Example 1: 创建镜像仓库镜像扫描任务配置**



Input: 

```
tccli csip CreateImageRegistryTimedScanTaskConfig --cli-unfold-argument  \
    --Name 手动定时任务1 \
    --Enable False \
    --ScanType 0 \
    --Schedule.CycleType DAILY \
    --Schedule.CycleDays 3 \
    --Schedule.StartTime 16:00 \
    --Schedule.Timezone Asia/Shanghai \
    --Target.Mode AUTO_MATCH \
    --Target.ExcludeImages 1 \
    --Target.Images 2 \
    --Target.AutoMatch.Modes BY_CLUSTER \
    --Target.AutoMatch.Clusters cls-ed8yg8pq \
    --Timeout 600
```

Output: 
```
{
    "Response": {
        "RequestId": "7c5c2594-1c4e-4717-93cf-8571534dfc59"
    }
}
```

