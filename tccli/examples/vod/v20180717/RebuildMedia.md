**Example 1: 发起音画质重生**

发起音画质重生

Input: 

```
tccli vod RebuildMedia --cli-unfold-argument  \
    --SuperResolutionInfo.Switch ON \
    --VideoFrameInterpolationInfo.Switch ON \
    --VideoFrameInterpolationInfo.Fps 25 \
    --FileId 8312960950918954859 \
    --RepairInfo.Switch ON \
    --TargetInfo.Container mp4 \
    --TargetInfo.MediaName 字符串 \
    --TargetInfo.Description 字符串
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxx-RebuildMedia-75e45d323ffad76987112fafe2eb87dxxx",
        "RequestId": "ef5aae86-6eab-4cb3-9ebc-0979010b3f22"
    }
}
```

