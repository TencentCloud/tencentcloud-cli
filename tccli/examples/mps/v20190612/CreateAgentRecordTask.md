**Example 1: 定时开始录制**



Input: 

```
tccli mps CreateAgentRecordTask --cli-unfold-argument  \
    --LiveRoomUrl https://****.******.com/*********** \
    --MaxDurationMinutes 1 \
    --StoreCosParam.CosBucketName ******-test-live-record-task-********** \
    --StoreCosParam.CosBucketRegion ap-guangzhou \
    --StoreCosParam.CosBucketPath record-only \
    --StartTime 2026-07-03T12:10:28.065902+08:00
```

Output: 
```
{
    "Response": {
        "TaskId": "task_857a704be0d4da429630928dc35f8b33",
        "RequestId": "7bf98ed1-4e2b-4be6-ab54-ae0f4d1e502d"
    }
}
```

**Example 2: 立即开始录制**



Input: 

```
tccli mps CreateAgentRecordTask --cli-unfold-argument  \
    --LiveRoomUrl https://****.******.com/*********** \
    --MaxDurationMinutes 1 \
    --StoreCosParam.CosBucketName ******-test-live-record-task-********** \
    --StoreCosParam.CosBucketRegion ap-guangzhou \
    --StoreCosParam.CosBucketPath record-only
```

Output: 
```
{
    "Response": {
        "TaskId": "task_9fac9a28f27292d8fbdf26e63beaeb03",
        "RequestId": "8a3e4c65-b473-456f-9158-57f3b0a5aff6"
    }
}
```

