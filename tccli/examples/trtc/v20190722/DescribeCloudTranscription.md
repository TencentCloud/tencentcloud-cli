**Example 1: 查询转录任务**



Input: 

```
tccli trtc DescribeCloudTranscription --cli-unfold-argument  \
    --TaskId m9-bVVU7nhKM5X3GsED6KNGVG********ndibWSn631uT6pbhE4PcPDSsggE. \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "StartTime": 1772433534515,
        "Status": "Idle",
        "RequestId": "f83001c5-7e3c-dfac-ba3e-236bf063c8d1",
        "TaskId": "m9-bVVU7nhKM5X3GsED6KNGVG********ndibWSn631uT6pbhE4PcPDSsggE."
    }
}
```

