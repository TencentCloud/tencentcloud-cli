**Example 1: 创建课后录制任务**

创建课后录制任务

Input: 

```
tccli tiw CreateOfflineRecord --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 8000 \
    --GroupId 8000 \
    --MixStream.Enabled true \
    --MixStream.ModelId 1 \
    --Whiteboard.Width 1280 \
    --Whiteboard.Height 960
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

