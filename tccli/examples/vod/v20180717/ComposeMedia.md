**Example 1: 对点播中的视频进行配音**

对 5285485487985271487 消除原来的音频，从5秒开始使用5285485487985271488进行配音，从20秒开始使用5285485487985271489的第2到第16秒进行配音，生成一个新的点播视频。

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Output.Container mp4 \
    --Output.FileName test \
    --Tracks.0.TrackItems.0.Type Empty \
    --Tracks.0.TrackItems.0.EmptyItem.Duration 5 \
    --Tracks.0.TrackItems.1.AudioItem.SourceMedia 5285485487985271488 \
    --Tracks.0.TrackItems.1.AudioItem.Duration 15 \
    --Tracks.0.TrackItems.1.Type Audio \
    --Tracks.0.TrackItems.2.AudioItem.Duration 14 \
    --Tracks.0.TrackItems.2.AudioItem.SourceMedia 5285485487985271489 \
    --Tracks.0.TrackItems.2.AudioItem.SourceMediaStartTime 2 \
    --Tracks.0.TrackItems.2.Type Audio \
    --Tracks.0.Type Audio \
    --Tracks.1.TrackItems.0.Type Video \
    --Tracks.1.TrackItems.0.VideoItem.SourceMedia 5285485487985271487 \
    --Tracks.1.TrackItems.0.VideoItem.AudioOperations.0.VolumeParam.Mute 1 \
    --Tracks.1.TrackItems.0.VideoItem.AudioOperations.0.Type Volume \
    --Tracks.1.Type Video
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-ComposeMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 2: 对两个视频流进行裁剪后拼接在一起**

取5285485487985271487的第2秒到第62秒，5285485487985271488的第6秒到81秒进行拼接，中间设置5秒的淡入淡出转场， 从视频的3秒到18秒贴上一个图片5285485487985271489，位置为（20px，20px），宽高为（100px，100px）。

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Output.Container mp4 \
    --Output.FileName test \
    --Tracks.0.TrackItems.0.StickerItem.CoordinateOrigin TopLeft \
    --Tracks.0.TrackItems.0.StickerItem.XPos 20px \
    --Tracks.0.TrackItems.0.StickerItem.YPos 20px \
    --Tracks.0.TrackItems.0.StickerItem.Height 100px \
    --Tracks.0.TrackItems.0.StickerItem.Width 100px \
    --Tracks.0.TrackItems.0.StickerItem.StartTime 3 \
    --Tracks.0.TrackItems.0.StickerItem.Duration 15 \
    --Tracks.0.TrackItems.0.StickerItem.SourceMedia 5285485487985271489 \
    --Tracks.0.TrackItems.0.Type Sticker \
    --Tracks.0.Type Sticker \
    --Tracks.1.TrackItems.0.TransitionItem.Duration 5 \
    --Tracks.1.TrackItems.0.TransitionItem.MediaTransitions.0.Type ImageFadeInFadeOut \
    --Tracks.1.TrackItems.0.Type Transition \
    --Tracks.1.TrackItems.1.Type Video \
    --Tracks.1.TrackItems.1.VideoItem.Duration 60 \
    --Tracks.1.TrackItems.1.VideoItem.SourceMedia 5285485487985271487 \
    --Tracks.1.TrackItems.1.VideoItem.SourceMediaStartTime 2 \
    --Tracks.1.TrackItems.2.Type Video \
    --Tracks.1.TrackItems.2.VideoItem.Duration 75 \
    --Tracks.1.TrackItems.2.VideoItem.SourceMedia 5285485487985271488 \
    --Tracks.1.TrackItems.2.VideoItem.SourceMediaStartTime 6 \
    --Tracks.1.Type Video
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-ComposeMedia-bffb15f07530b57bc1aabb01fac74bc2"
    }
}
```

**Example 3: 将一个视频作为另一个视频的画中画**

将5285485487985271487的视频作为画中画的主画面；将5285485487985271488的视频作为画中画的子画面；子画面的中心偏移主画面25%（即在主画面右下角），宽度占画面的30%。

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Output.Container mp4 \
    --Output.FileName test \
    --Tracks.0.TrackItems.0.Type Video \
    --Tracks.0.TrackItems.0.VideoItem.SourceMedia 5285485487985271487 \
    --Tracks.0.Type Video \
    --Tracks.1.TrackItems.0.Type Video \
    --Tracks.1.TrackItems.0.VideoItem.CoordinateOrigin Center \
    --Tracks.1.TrackItems.0.VideoItem.Width 30% \
    --Tracks.1.TrackItems.0.VideoItem.SourceMedia 5285485487985271488 \
    --Tracks.1.TrackItems.0.VideoItem.XPos 25% \
    --Tracks.1.TrackItems.0.VideoItem.YPos 25% \
    --Tracks.1.Type Video
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-ComposeMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

