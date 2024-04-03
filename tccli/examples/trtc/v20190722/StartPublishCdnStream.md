**Example 1: 发起混流转推**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomId 195044 \
    --AudioParams.SubscribeAudioList.0.UserInfo.UserId Trtc_User_0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomId 195044 \
    --AudioParams.SubscribeAudioList.1.UserInfo.UserId Trtc_User_1 \
    --AudioParams.SubscribeAudioList.2.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.2.UserInfo.RoomId 195044 \
    --AudioParams.SubscribeAudioList.2.UserInfo.UserId Trtc_User_2 \
    --AudioParams.SubscribeAudioList.3.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.3.UserInfo.RoomId 195044 \
    --AudioParams.SubscribeAudioList.3.UserInfo.UserId Trtc_User_3 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 512 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.PureAudioHoldPlaceMode 0 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 195044 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 360 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomId 195044 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.UserId Trtc_User_1 \
    --VideoParams.LayoutParams.MixLayoutList.1.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageHeight 360 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.2.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.2.LocationY 360 \
    --VideoParams.LayoutParams.MixLayoutList.2.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.2.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.2.UserMediaStream.UserInfo.RoomId 195044 \
    --VideoParams.LayoutParams.MixLayoutList.2.UserMediaStream.UserInfo.UserId Trtc_User_2 \
    --VideoParams.LayoutParams.MixLayoutList.2.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.2.ImageHeight 360 \
    --VideoParams.LayoutParams.MixLayoutList.2.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.2.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.3.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.3.LocationY 360 \
    --VideoParams.LayoutParams.MixLayoutList.3.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.3.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.3.UserMediaStream.UserInfo.RoomId 195044 \
    --VideoParams.LayoutParams.MixLayoutList.3.UserMediaStream.UserInfo.UserId Trtc_User_3 \
    --VideoParams.LayoutParams.MixLayoutList.3.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.3.ImageHeight 360 \
    --VideoParams.LayoutParams.MixLayoutList.3.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.3.RenderMode 0 \
    --VideoParams.BackGroundColor 0xFF0000 \
    --VideoParams.WaterMarkList.0.WaterMarkType 0 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationX 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationY 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkHeight 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkWidth 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkUrl https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png \
    --VideoParams.WaterMarkList.0.WaterMarkImage.ZOrder 3 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 0 \
    --PublishCdnParams.1.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test2 \
    --PublishCdnParams.1.IsTencentCdn 0 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 195044
```

Output: 
```
{
    "Response": {
        "TaskId": "-m97l2ZU7vxyBSmXYsRx1Xy9Kf4bVVfbbhSKC4K-4pycoZWKv542xbi139uTvGt1zAHoAQ..",
        "RequestId": "b934c535-8d82-4f52-bd52-a1cbb043c4be"
    }
}
```

**Example 2: 发起单流纯音频旁路转推**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --SingleSubscribeParams.UserMediaStream.StreamType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomIdType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomId 195044 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 0 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 0 \
    --RoomId 195044
```

Output: 
```
{
    "Response": {
        "TaskId": "-m97l2ZU7r57nZBesMa84KgzxhH0OBbbCRaKC4K-4pycoZW7yFPtusNuZOen1Ca0qtQQAQ..",
        "RequestId": "ef089f8b-d0d1-4131-894d-4edd68d61605"
    }
}
```

**Example 3: 发起单流音视频旁路转推**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 512 \
    --VideoParams.VideoEncode.Gop 2 \
    --SingleSubscribeParams.UserMediaStream.StreamType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomIdType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomId 195044 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 0 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 0 \
    --RoomId 195044
```

Output: 
```
{
    "Response": {
        "TaskId": "-m97l2ZU7tq6nEsHR89259B8aCDblqnbGhWKC4K-4pycoZWpyHnld1jC9aCD+EU7V8WRAQ..",
        "RequestId": "f23d95bf-ddaf-4d0c-86c0-6bf50c74c0a0"
    }
}
```

**Example 4: 混一个人的音视频，和房间所有人的声音**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AgentParams.MaxIdleTime 10 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 512 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId 57906 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 1280 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/1400188366_owen_main_1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
```

Output: 
```
{
    "Response": {
        "TaskId": "-m9liFNU7qjpXnrk6cloz8KXukyLKjzbLhP2AYK-4pycoZVbtyt6U21l9vJOqqeIfwR5AQ..",
        "RequestId": "97dae8e4-4778-45c8-9abe-cdce33c1a450"
    }
}
```

**Example 5: 音视频上行，只混纯音频，和透传上行SEI**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomId 295066 \
    --AudioParams.SubscribeAudioList.0.UserInfo.UserId 57906 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AgentParams.MaxIdleTime 10 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 512 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId 57906 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/1400188366_owen_main_1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
```

Output: 
```
{
    "Response": {
        "TaskId": "-m9liFNU7m+nWPL+icY53kcSoQ+-czzbEhD2AYK-4pycoZXmj3cMGzreW5xwhHTpcPRNAQ..",
        "RequestId": "6774662b-64a0-4aec-8389-0513873585b4"
    }
}
```

