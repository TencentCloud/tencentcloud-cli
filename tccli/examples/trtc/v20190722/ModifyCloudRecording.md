**Example 1: 更新云端录制**

更新SdkAppId 为 1400188366 TaskId 为-m9-bVVU7gzdSqvsV***Y+QMYNee2QE.的云端录制，设置视频流订阅白名单user1，user2，设置音频流订阅白名单user1，user2。设置自定义布局模式。

Input: 

```
tccli trtc ModifyCloudRecording --cli-unfold-argument  \
    --SubscribeStreamUserIds.SubscribeVideoUserIds user1 user2 \
    --SubscribeStreamUserIds.SubscribeAudioUserIds user1 user2 \
    --TaskId -m9-bVVU7gzdSqvsV***Y+QMYNee2QE. \
    --SdkAppId 1400188366 \
    --MixLayoutParams.MixLayoutMode 4 \
    --MixLayoutParams.MixLayoutList.0.Top 100 \
    --MixLayoutParams.MixLayoutList.0.UserId user1 \
    --MixLayoutParams.MixLayoutList.0.Height 100 \
    --MixLayoutParams.MixLayoutList.0.Width 100 \
    --MixLayoutParams.MixLayoutList.0.Left 100 \
    --MixLayoutParams.MixLayoutList.1.Top 200 \
    --MixLayoutParams.MixLayoutList.1.UserId user2 \
    --MixLayoutParams.MixLayoutList.1.Height 100 \
    --MixLayoutParams.MixLayoutList.1.Width 100 \
    --MixLayoutParams.MixLayoutList.1.Left 200
```

Output: 
```
{
    "Response": {
        "TaskId": "-m9-bVVU7gzdSqvsV***Y+QMYNee2QE.",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

