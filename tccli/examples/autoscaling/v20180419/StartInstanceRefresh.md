**Example 1: 滚动更新方式进行实例刷新**

将伸缩组 asg-9dn1a5y6 中的实例分成 3 个批次进行滚动更新，批次间会自动暂停。

Input: 

```
tccli as StartInstanceRefresh --cli-unfold-argument  \
    --AutoScalingGroupId asg-9dn1a5y6 \
    --RefreshMode ROLLING_UPDATE \
    --RefreshSettings.RollingUpdateSettings.BatchNumber 3 \
    --RefreshSettings.RollingUpdateSettings.BatchPause BATCH_INTERVAL_PAUSE
```

Output: 
```
{
    "Response": {
        "RefreshActivityId": "asr-y67t5r4e",
        "RequestId": "c4190090-bc60-4f48-b9d4-48095b9596db"
    }
}
```

