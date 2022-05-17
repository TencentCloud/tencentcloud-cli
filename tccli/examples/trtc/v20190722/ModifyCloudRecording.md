**Example 1: 更新云端录制**

更新SdkAppId 为 1234 TaskId 为xx 的云端录制，设置视频流订阅白名单123，456，设置音频流订阅白名单123，456。设置自定义布局模式。

Input: 

```
tccli trtc ModifyCloudRecording --cli-unfold-argument  \
    --SubscribeStreamUserIds.SubscribeVideoUserIds 123 456 \
    --SubscribeStreamUserIds.SubscribeAudioUserIds 123 456 \
    --TaskId xx \
    --SdkAppId 1234 \
    --MixLayoutParams.MixLayoutMode 4 \
    --MixLayoutParams.MixLayoutList.0.Top 100 \
    --MixLayoutParams.MixLayoutList.0.UserId 123 \
    --MixLayoutParams.MixLayoutList.0.Height 100 \
    --MixLayoutParams.MixLayoutList.0.Width 100 \
    --MixLayoutParams.MixLayoutList.0.Left 100 \
    --MixLayoutParams.MixLayoutList.1.Top 200 \
    --MixLayoutParams.MixLayoutList.1.UserId 456 \
    --MixLayoutParams.MixLayoutList.1.Height 100 \
    --MixLayoutParams.MixLayoutList.1.Width 100 \
    --MixLayoutParams.MixLayoutList.1.Left 200
```

Output: 
```
{
    "Response": {
        "TaskId": "5df46eb2-8e4b-490e-9c3c-dbd3b84faefc",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

