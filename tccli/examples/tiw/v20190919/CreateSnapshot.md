**Example 1: 创建快照任务**

创建快照任务

Input: 

```
tccli tiw CreateSnapshot --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 2322232 \
    --SnapshotMode Period \
    --SnapshotPeriod 10 \
    --CosBucket.Name snapshot-result \
    --CosBucket.Region ap-shanghai \
    --CosBucket.Path snapshot \
    --CosBucket.ResultDomain https://cdn.example.com
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "g6ls63ps49vteb8bk1mb"
    }
}
```

