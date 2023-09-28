**Example 1: 滚动更新方式回滚实例刷新活动**

对伸缩组 asg-9dn1a5y6 的实例刷新活动 asr-i8u7tytd 进行回滚。

Input: 

```
tccli as RollbackInstanceRefresh --cli-unfold-argument  \
    --AutoScalingGroupId asg-9dn1a5y6 \
    --RefreshMode ROLLING_UPDATE \
    --OriginRefreshActivityId asr-i8u7tytd \
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

