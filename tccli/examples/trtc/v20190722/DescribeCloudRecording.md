**Example 1: 查询SdkAppId 为 1400***366 TaskId 为 m9-bVVU7nhKM5X3GsED6KNGVG********ndibWSn631uT6pbhE4PcPDSsggE.的录制状态。**



Input: 

```
tccli trtc DescribeCloudRecording --cli-unfold-argument  \
    --TaskId m9-bVVU7nhKM5X3GsED6KNGVG********ndibWSn631uT6pbhE4PcPDSsggE. \
    --SdkAppId 1400188366
```

Output: 
```
{
    "Response": {
        "Status": "InProgress",
        "StorageFileList": [],
        "RequestId": "c4536bd1-c3ea-4e84-b2dd-a8491d2057e2",
        "TaskId": "m9-bVVU7nhKM5X3GsED6KNGVG********ndibWSn631uT6pbhE4PcPDSsggE."
    }
}
```

