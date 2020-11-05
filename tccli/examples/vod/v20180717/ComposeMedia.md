**Example 1: Clipping and splicing two video streams**

This example shows you how to take the 2nd to 62nd seconds of `5285485487985271487` and the 6th to 81st seconds of `5285485487985271488` for splicing, set a fade-in/fade-out transition of 5 seconds in between, and paste image `5285485487985271489` with width and height of (100px, 100px) between the 3rd and 18th seconds of the video at the position of (20px, 20px).

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Tracks.0.Type Video\
    --Tracks.0.TrackItems.0.Type Video\
    --Tracks.0.TrackItems.0.VideoItem.SourceMedia 5285485487985271487\
    --Tracks.0.TrackItems.0.VideoItem.SourceMediaStartTime 2\
    --Tracks.0.TrackItems.0.VideoItem.Duration 60\
    --Tracks.0.TrackItems.1.Type Transition\
    --Tracks.0.TrackItems.1.TransitionItem.Duration 5\
    --Tracks.0.TrackItems.1.TransitionItem.TransitionOperations.0.Type ImageFadeInFadeOut\
    --Tracks.0.TrackItems.2.Type Video\
    --Tracks.0.TrackItems.2.VideoItem.SourceMedia 5285485487985271488\
    --Tracks.0.TrackItems.2.VideoItem.SourceMediaStartTime 6\
    --Tracks.0.TrackItems.2.VideoItem.Duration 75\
    --Tracks.1.Type Sticker\
    --Tracks.1.TrackItems.0.Type Sticker\
    --Tracks.1.TrackItems.0.StickerItem.SourceMedia 5285485487985271489\
    --Tracks.1.TrackItems.0.StickerItem.StartTime 3\
    --Tracks.1.TrackItems.0.StickerItem.Duration 15\
    --Tracks.1.TrackItems.0.StickerItem.CoordinateOrigin TopLeft\
    --Tracks.1.TrackItems.0.StickerItem.XPos 20px\
    --Tracks.1.TrackItems.0.StickerItem.YPos 20px\
    --Tracks.1.TrackItems.0.StickerItem.Width 100px\
    --Tracks.1.TrackItems.0.StickerItem.Height 100px\
    --Output.FileName test\
    --Output.Container mp4
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

**Example 2: Dubbing a VOD video**

This example shows you how to remove the original audio from `5285485487985271487`, dub it starting from the 5th second with `5285485487985271488`, and dub it starting from the 20th second with the 2nd to 16th seconds of `5285485487985271489` to generate a new VOD video.

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Tracks.0.Type Video\
    --Tracks.0.TrackItems.0.Type Video\
    --Tracks.0.TrackItems.0.VideoItem.SourceMedia 5285485487985271487\
    --Tracks.0.TrackItems.0.VideoItem.AudioOperations.0.Type Volume\
    --Tracks.0.TrackItems.0.VideoItem.AudioOperations.0.VolumeParam.Mute 1\
    --Tracks.1.Type Audio\
    --Tracks.1.TrackItems.0.Type Empty\
    --Tracks.1.TrackItems.0.EmptyItem.Duration 5\
    --Tracks.1.TrackItems.1.Type Audio\
    --Tracks.1.TrackItems.1.AudioItem.SourceMedia 5285485487985271488\
    --Tracks.1.TrackItems.1.AudioItem.Duratiion 15\
    --Tracks.1.TrackItems.2.Type Audio\
    --Tracks.1.TrackItems.2.AudioItem.SourceMedia 5285485487985271489\
    --Tracks.1.TrackItems.2.AudioItem.SourceMediaStartTime 2\
    --Tracks.1.TrackItems.2.AudioItem.Duration 14\
    --Output.FileName test\
    --Output.Container mp4
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

**Example 3: Playing two videos in picture-in-picture mode**

This example shows you how to play the `5285485487985271487` video as the primary image and the `5285485487985271488` video as the small image in picture-in-picture mode. The small image is displayed in the lower right corner of the primary image with their centers offset by 25%, and the width of the small image is 30% of that of the primary image.

Input: 

```
tccli vod ComposeMedia --cli-unfold-argument  \
    --Tracks.0.Type Video\
    --Tracks.0.TrackItems.0.Type Video\
    --Tracks.0.TrackItems.0.VideoItem.SourceMedia 5285485487985271487\
    --Tracks.1.Type Video\
    --Tracks.1.TrackItems.0.Type Video\
    --Tracks.1.TrackItems.0.VideoItem.SourceMedia 5285485487985271488\
    --Tracks.1.TrackItems.0.VideoItem.CoordinateOrigin Center\
    --Tracks.1.TrackItems.0.VideoItem.XPos 25%\
    --Tracks.1.TrackItems.0.VideoItem.YPos 25%\
    --Tracks.1.TrackItems.0.VideoItem.Width 30%\
    --Output.FileName test\
    --Output.Container mp4
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

