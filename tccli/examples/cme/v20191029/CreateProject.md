**Example 1: 创建普通剪辑项目**

 

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category VIDEO_EDIT \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name first_project \
    --AspectRatio 16:9
```

Output: 
```
{
    "Response": {
        "ProjectId": "cmepid_5f16967b64436100015fb025",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 2: 创建一个导播台项目**

 

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category SWITCHER \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name 导播台 \
    --SwitcherProjectInput.PgmOutputConfig.TemplateId 10001
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f29",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5c"
    }
}
```

**Example 3: 使用初始轨道创建项目**

 

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category VIDEO_EDIT \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name 视频剪辑项目并初始化轨道 \
    --VideoEditProjectInput.InitTracks.0.TrackItems.0.Type Video \
    --VideoEditProjectInput.InitTracks.0.TrackItems.0.VideoItem.Duration 10 \
    --VideoEditProjectInput.InitTracks.0.TrackItems.0.VideoItem.SourceMedia 52858908113623182311 \
    --VideoEditProjectInput.InitTracks.0.TrackItems.0.VideoItem.SourceMediaStartTime 0 \
    --VideoEditProjectInput.InitTracks.0.TrackItems.0.VideoItem.SourceType VOD \
    --VideoEditProjectInput.InitTracks.0.Type Video \
    --VideoEditProjectInput.AspectRatio 16:9
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f31",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e6a"
    }
}
```

**Example 4: 使用剪辑模板创建项目**

 

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category VIDEO_EDIT \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name 剪辑模板项目 \
    --VideoEditProjectInput.AspectRatio 16:9 \
    --VideoEditProjectInput.VideoEditTemplateId 61385efc24827f05859d3765@Public@CME
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f30",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5a"
    }
}
```

**Example 5: 创建一个云转推项目，初始化输入源为直播拉流**

云转推项目初始化输入输出源

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category STREAM_CONNECT \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name stream_connect \
    --StreamConnectProjectInput.MainInput.LivePullInputInfo.InputUrl rtmp://liveplay.video-studio.myqcloud.com/output/1250000001-600e8e7fb1cc1c0001293759 \
    --StreamConnectProjectInput.MainInput.InputType LivePull \
    --StreamConnectProjectInput.Outputs.0.PushUrl rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f29",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 6: 创建一个云转推项目，初始化输入源为直播推流**

云转推项目初始化输入输出源

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category STREAM_CONNECT \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name 云转推 \
    --StreamConnectProjectInput.MainInput.InputType RtmpPush \
    --StreamConnectProjectInput.MainInput.RtmpPushInputInfo.ExpiredSecond 3600 \
    --StreamConnectProjectInput.Outputs.0.PushUrl rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f29",
        "RtmpPushInputInfoSet": [
            {
                "ExpiredSecond": 3600,
                "PushUrl": "rtmp://livepush-xx.video-studio.myqcloud.com/output/1250000001-6086674e265b450001837f8e?txSecret=4478cfdfe0fd0eb3820705aebaa328xx&txTime=608FA1CE"
            },
            {
                "ExpiredSecond": 0,
                "PushUrl": ""
            }
        ],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 7: 创建一个点播转直播项目，播放一次，输出视频的帧率为25帧，码率为2500K，视频大小为1920*1080。**

 

Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Category MEDIA_CAST \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_61978823e6a253000100fb0f \
    --Name 点播转直播项目 \
    --MediaCastProjectInput.PlaySetting.LoopCount 1 \
    --MediaCastProjectInput.OutputMediaSetting.VideoSetting.Width 1920 \
    --MediaCastProjectInput.OutputMediaSetting.VideoSetting.FrameRate 25 \
    --MediaCastProjectInput.OutputMediaSetting.VideoSetting.Bitrate 2500 \
    --MediaCastProjectInput.OutputMediaSetting.VideoSetting.Height 1080 \
    --MediaCastProjectInput.SourceInfos.0.Type VOD \
    --MediaCastProjectInput.SourceInfos.0.FileId 122 \
    --MediaCastProjectInput.SourceInfos.1.Type CME \
    --MediaCastProjectInput.SourceInfos.1.MaterialId aaa12323 \
    --MediaCastProjectInput.DestinationInfos.0.PushUrl rtmp://livetest.com/live/a?t=11 \
    --MediaCastProjectInput.DestinationInfos.0.Name test
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f31",
        "RtmpPushInputInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e6a"
    }
}
```

