**Example 1: 更新转推参数**

无

Input: 

```
tccli trtc UpdatePublishCdnStream --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --TaskId -m97l2ZU7kOlV5cTRMoU6yoGp2nDYkzbJ13EC4K-4pycoZXVv+XVrNoUXQ8++8Z2PwUlAQ.. \
    --SequenceNumber 20 \
    --WithTranscoding 1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test2?bizid=3891&txSecret=23aeb6ec16fd275af0d00a447b2282f7&txTime=62635BDE
```

Output: 
```
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f",
        "TaskId": "xxxx"
    }
}
```

**Example 2: 更新混音和布局参数**

更新为混主播Trtc_User_0和Trtc_User_3的音视频。

Input: 

```
tccli trtc UpdatePublishCdnStream --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --TaskId -m97l2ZU7kOlV5cTRMoU6yoGp2nDYkzbJ13EC4K-4pycoZXVv+XVrNoUXQ8++8Z2PwUlAQ.. \
    --SequenceNumber 20 \
    --WithTranscoding 1 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomId 48111 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.0.UserInfo.UserId Trtc_User_0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomId 48111 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.UserId Trtc_User_3 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 48111 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId Trtc_User_3 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomId 48111 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationY 360 \
    --VideoParams.LayoutParams.MixLayoutList.1.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.RenderMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f",
        "TaskId": "xxxx"
    }
}
```

