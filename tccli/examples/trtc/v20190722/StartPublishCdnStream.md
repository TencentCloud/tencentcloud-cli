**Example 1: 发起音视频混流转推 CDN**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 1536 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.PureAudioHoldPlaceMode 0 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.UserId Trtc_User_1 \
    --VideoParams.LayoutParams.MixLayoutList.1.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.RenderMode 0 \
    --VideoParams.BackGroundColor 0xFF0000 \
    --VideoParams.WaterMarkList.0.WaterMarkType 0 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationX 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationY 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkHeight 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkWidth 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkUrl https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png \
    --VideoParams.WaterMarkList.0.WaterMarkImage.ZOrder 3 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
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

**Example 2: 发起纯音频混流转推 CDN**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.0.UserInfo.RoomId 295066 \
    --AudioParams.SubscribeAudioList.0.UserInfo.UserId Trtc_User_0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomIdType 0 \
    --AudioParams.SubscribeAudioList.1.UserInfo.RoomId 295066 \
    --AudioParams.SubscribeAudioList.1.UserInfo.UserId Trtc_User_1 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
```

Output: 
```
{
    "Response": {
        "RequestId": "388014ec-a0b8-4b8f-86bc-1f467448f5f0",
        "TaskId": "-m9lnV5U7nj4rkLBWMXF9n8-EohONCXbalWuLYK-4pycoZWQndibcqSVnrlqKF5om7EIDVk4awE."
    }
}
```

**Example 3: 发起单流音视频旁路转推 CDN**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 1536 \
    --VideoParams.VideoEncode.Gop 2 \
    --SingleSubscribeParams.UserMediaStream.StreamType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomIdType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomId 295066 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 0 \
    --RoomId 295066
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

**Example 4: 发起单流纯音频旁路转推 CDN**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --SingleSubscribeParams.UserMediaStream.StreamType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomIdType 0 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.RoomId 295066 \
    --SingleSubscribeParams.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 0 \
    --RoomId 295066
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

**Example 5: 发起音视频混流回推 TRTC 房间**



Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 1536 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.PureAudioHoldPlaceMode 0 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.UserId Trtc_User_1 \
    --VideoParams.LayoutParams.MixLayoutList.1.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.RenderMode 0 \
    --VideoParams.BackGroundColor 0xFF0000 \
    --VideoParams.WaterMarkList.0.WaterMarkType 0 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationX 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationY 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkHeight 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkWidth 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkUrl https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png \
    --VideoParams.WaterMarkList.0.WaterMarkImage.ZOrder 3 \
    --FeedBackRoomParams.0.RoomId 630777 \
    --FeedBackRoomParams.0.RoomIdType 0 \
    --FeedBackRoomParams.0.UserId trtc_partner_test_2 \
    --FeedBackRoomParams.0.UserSig eJwtjEELgjAYhv-Ldy10m7mtQYcQOtklU6mLSFs1LVnzq4Tovwfa8Xmel-cD*zQLXsaDAhYQmI9stenQnu2o0eOpcrXHzvgKTY8V*8963dbOWQ2KLgihUkacTwXt3YCigpIlo0KyyZrBWW9ARZyQ-4O9gIJrYfK365M85PEw02HZPneNaJJbg4-1Nj6KQqZZacVhI1fw-QEkCzYe \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
```

Output: 
```
{
    "Response": {
        "RequestId": "921e9cf6-b77c-4a7a-ab0e-c66a3e66fc59",
        "TaskId": "-m9lnV5U7n7TwoLKSsii1JivUn7DLDDbP16uLYK-4pycoZWQndib8GQJZEMMXFyOHe9Ds6WfxAE."
    }
}
```

**Example 6: 发起音视频混流转推 CDN ，输出数据带布局 SEI**

无

Input: 

```
tccli trtc StartPublishCdnStream --cli-unfold-argument  \
    --AgentParams.MaxIdleTime 30 \
    --AgentParams.UserSig eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_ \
    --AgentParams.UserId trtc_partner_test_1 \
    --AudioParams.AudioEncode.SampleRate 48000 \
    --AudioParams.AudioEncode.Codec 0 \
    --AudioParams.AudioEncode.BitRate 64 \
    --AudioParams.AudioEncode.Channel 2 \
    --VideoParams.VideoEncode.Height 720 \
    --VideoParams.VideoEncode.Width 1280 \
    --VideoParams.VideoEncode.Fps 15 \
    --VideoParams.VideoEncode.BitRate 1536 \
    --VideoParams.VideoEncode.Gop 2 \
    --VideoParams.LayoutParams.PureAudioHoldPlaceMode 0 \
    --VideoParams.LayoutParams.MixLayoutMode 4 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationX 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.0.UserMediaStream.UserInfo.UserId Trtc_User_0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.0.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.0.RenderMode 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationX 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.LocationY 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.StreamType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomIdType 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.RoomId 295066 \
    --VideoParams.LayoutParams.MixLayoutList.1.UserMediaStream.UserInfo.UserId Trtc_User_1 \
    --VideoParams.LayoutParams.MixLayoutList.1.ZOrder 0 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageHeight 720 \
    --VideoParams.LayoutParams.MixLayoutList.1.ImageWidth 640 \
    --VideoParams.LayoutParams.MixLayoutList.1.RenderMode 0 \
    --VideoParams.BackGroundColor 0xFF0000 \
    --VideoParams.WaterMarkList.0.WaterMarkType 0 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationX 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.LocationY 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkHeight 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkWidth 64 \
    --VideoParams.WaterMarkList.0.WaterMarkImage.WaterMarkUrl https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png \
    --VideoParams.WaterMarkList.0.WaterMarkImage.ZOrder 3 \
    --SeiParams.LayoutVolume.AppData layout_sei_test \
    --SeiParams.LayoutVolume.PayloadType 100 \
    --SeiParams.LayoutVolume.Interval 1000 \
    --SeiParams.LayoutVolume.FollowIdr 1 \
    --PublishCdnParams.0.PublishCdnUrl rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1 \
    --PublishCdnParams.0.IsTencentCdn 1 \
    --RoomIdType 0 \
    --SdkAppId 1400188366 \
    --WithTranscoding 1 \
    --RoomId 295066
```

Output: 
```
{
    "Response": {
        "RequestId": "6dfc18cc-2123-4a11-9591-f1e873fbbd65",
        "TaskId": "-m9lnV5U7nzo2Xwh48Dc-YCDrR5Bk8DbJ1WrLYK-4pycoZWQndibrNig9cq-7ljX4SenbKWlZAE."
    }
}
```

