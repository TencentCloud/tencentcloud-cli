**Example 1: 重置目标检测服务**



Input: 

```
tccli iotexplorer ResetCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --ServiceType RealtimeObjectDetect
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f"
    }
}
```

**Example 2: 重置视频浓缩服务**



Input: 

```
tccli iotexplorer ResetCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --ServiceType Highlight
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f"
    }
}
```

**Example 3: 重置指定通道的云存 AI 服务**

传入 ChannelId 指定要操作的通道

Input: 

```
tccli iotexplorer ResetCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --ServiceType Highlight \
    --ChannelId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f"
    }
}
```

