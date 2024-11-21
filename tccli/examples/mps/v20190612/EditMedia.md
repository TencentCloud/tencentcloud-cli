**Example 1: 【剪辑任务】对一个文件进行剪辑，生成一个新的视频**



Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.InputInfo.Type COS \
    --FileInfos.0.InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --FileInfos.0.InputInfo.CosInputInfo.Region ap-chongqing \
    --FileInfos.0.InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov \
    --FileInfos.0.StartTimeOffset 60.0 \
    --FileInfos.0.EndTimeOffset 120.0 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket TopRankVideo-125xxx88 \
    --OutputStorage.CosOutputStorage.Region ap-chongqing \
    --OutputObjectPath /clip_result/clip_WildAnimal.{format}
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 2: 【合成任务】图片&音频合成视频**

将一组图片和背景音乐拼接成一个视频，图片之间添加转场效果。轨道形式如下：
<img width="70%" src="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/01_img_audio_to_video/track.png" />

<a target="_blank" href="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/01_img_audio_to_video/01_img_audio_to_video.mp4">效果示例</a>

注：转场会消耗前后元素的轨道时长，如果一个元素前后有转场，则需要保证给元素的轨道时长大于前后两个转场的时间和。




Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.Id img01 \
    --FileInfos.0.InputInfo.Type URL \
    --FileInfos.0.InputInfo.UrlInputInfo.Url https://.../1.jpg \
    --FileInfos.1.Id img02 \
    --FileInfos.1.InputInfo.Type URL \
    --FileInfos.1.InputInfo.UrlInputInfo.Url https://.../2.jpg \
    --FileInfos.2.Id img03 \
    --FileInfos.2.InputInfo.Type URL \
    --FileInfos.2.InputInfo.UrlInputInfo.Url https://.../3.jpg \
    --FileInfos.3.Id img04 \
    --FileInfos.3.InputInfo.Type URL \
    --FileInfos.3.InputInfo.UrlInputInfo.Url https://.../4.jpg \
    --FileInfos.4.Id img05 \
    --FileInfos.4.InputInfo.Type URL \
    --FileInfos.4.InputInfo.UrlInputInfo.Url https://.../5.jpg \
    --FileInfos.5.Id img06 \
    --FileInfos.5.InputInfo.Type URL \
    --FileInfos.5.InputInfo.UrlInputInfo.Url https://.../6.jpg \
    --FileInfos.6.Id img07 \
    --FileInfos.6.InputInfo.Type URL \
    --FileInfos.6.InputInfo.UrlInputInfo.Url https://.../7.jpg \
    --FileInfos.7.Id img08 \
    --FileInfos.7.InputInfo.Type URL \
    --FileInfos.7.InputInfo.UrlInputInfo.Url https://.../8.jpg \
    --FileInfos.8.Id img09 \
    --FileInfos.8.InputInfo.Type URL \
    --FileInfos.8.InputInfo.UrlInputInfo.Url https://.../9.jpg \
    --FileInfos.9.Id img10 \
    --FileInfos.9.InputInfo.Type URL \
    --FileInfos.9.InputInfo.UrlInputInfo.Url https://.../10.jpg \
    --FileInfos.10.Id adu \
    --FileInfos.10.InputInfo.Type URL \
    --FileInfos.10.InputInfo.UrlInputInfo.Url https://.../back_music.mp3 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket your_bucket \
    --OutputStorage.CosOutputStorage.Region your_bucket_region \
    --OutputObjectPath /your/output/dir/ \
    --ComposeConfig.TargetInfo.Container mp4 \
    --ComposeConfig.TargetInfo.VideoStream.Fps 30 \
    --ComposeConfig.Tracks.0.Type Video \
    --ComposeConfig.Tracks.0.Items.0.Type Image \
    --ComposeConfig.Tracks.0.Items.0.Image.SourceMedia.FileId img01 \
    --ComposeConfig.Tracks.0.Items.0.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.1.Type Transition \
    --ComposeConfig.Tracks.0.Items.1.Transition.Transitions.0.Type Dreamy \
    --ComposeConfig.Tracks.0.Items.2.Type Image \
    --ComposeConfig.Tracks.0.Items.2.Image.SourceMedia.FileId img02 \
    --ComposeConfig.Tracks.0.Items.2.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.3.Type Transition \
    --ComposeConfig.Tracks.0.Items.3.Transition.Transitions.0.Type Circleopen \
    --ComposeConfig.Tracks.0.Items.4.Type Image \
    --ComposeConfig.Tracks.0.Items.4.Image.SourceMedia.FileId img03 \
    --ComposeConfig.Tracks.0.Items.4.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.5.Type Transition \
    --ComposeConfig.Tracks.0.Items.5.Transition.Transitions.0.Type Heart \
    --ComposeConfig.Tracks.0.Items.6.Type Image \
    --ComposeConfig.Tracks.0.Items.6.Image.SourceMedia.FileId img04 \
    --ComposeConfig.Tracks.0.Items.6.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.7.Type Transition \
    --ComposeConfig.Tracks.0.Items.7.Transition.Transitions.0.Type PolarFunction \
    --ComposeConfig.Tracks.0.Items.8.Type Image \
    --ComposeConfig.Tracks.0.Items.8.Image.SourceMedia.FileId img05 \
    --ComposeConfig.Tracks.0.Items.8.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.9.Type Transition \
    --ComposeConfig.Tracks.0.Items.9.Transition.Transitions.0.Type Swirl \
    --ComposeConfig.Tracks.0.Items.10.Type Image \
    --ComposeConfig.Tracks.0.Items.10.Image.SourceMedia.FileId img06 \
    --ComposeConfig.Tracks.0.Items.10.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.11.Type Transition \
    --ComposeConfig.Tracks.0.Items.11.Transition.Transitions.0.Type WipeRight \
    --ComposeConfig.Tracks.0.Items.12.Type Image \
    --ComposeConfig.Tracks.0.Items.12.Image.SourceMedia.FileId img07 \
    --ComposeConfig.Tracks.0.Items.12.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.13.Type Transition \
    --ComposeConfig.Tracks.0.Items.13.Transition.Transitions.0.Type ZoomInCircles \
    --ComposeConfig.Tracks.0.Items.14.Type Image \
    --ComposeConfig.Tracks.0.Items.14.Image.SourceMedia.FileId img08 \
    --ComposeConfig.Tracks.0.Items.14.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.15.Type Transition \
    --ComposeConfig.Tracks.0.Items.15.Transition.Transitions.0.Type ImageFadeInFadeOut \
    --ComposeConfig.Tracks.0.Items.16.Type Image \
    --ComposeConfig.Tracks.0.Items.16.Image.SourceMedia.FileId img09 \
    --ComposeConfig.Tracks.0.Items.16.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.0.Items.17.Type Transition \
    --ComposeConfig.Tracks.0.Items.17.Transition.Transitions.0.Type ButterflyWaveScrawler \
    --ComposeConfig.Tracks.0.Items.18.Type Image \
    --ComposeConfig.Tracks.0.Items.18.Image.SourceMedia.FileId img10 \
    --ComposeConfig.Tracks.0.Items.18.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.1.Type Audio \
    --ComposeConfig.Tracks.1.Items.0.Type Audio \
    --ComposeConfig.Tracks.1.Items.0.Audio.SourceMedia.FileId adu \
    --ComposeConfig.Tracks.1.Items.0.Audio.TrackTime.Duration 21s
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 3: 【合成任务】剪辑&片头&片尾&水印图片&文字&音频替换**

剪辑一个视频，并给视频添加片头、片尾、水印图片、说明文字、替换音频，合成一个新的视频。轨道形式如下：
<img width="50%" src="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/02_video_start_end_logo_txt/track.png" />

<a target="_blank" href="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/02_video_start_end_logo_txt/02_video_start_end_logo_txt.mp4">效果示例</a>

注：片头和片尾可以是视频，也可以是图片。
注：Canvas 参数用于指定输出视频大小，如果不填将默认使用第一个视频大小，所以建议将正品视频放在素材列表的第一个。


Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.Id start \
    --FileInfos.0.InputInfo.Type URL \
    --FileInfos.0.InputInfo.UrlInputInfo.Url https://.../start.mp4 \
    --FileInfos.1.Id video \
    --FileInfos.1.InputInfo.Type URL \
    --FileInfos.1.InputInfo.UrlInputInfo.Url https://.../video.mp4 \
    --FileInfos.2.Id end \
    --FileInfos.2.InputInfo.Type URL \
    --FileInfos.2.InputInfo.UrlInputInfo.Url https://.../end.png \
    --FileInfos.3.Id img \
    --FileInfos.3.InputInfo.Type URL \
    --FileInfos.3.InputInfo.UrlInputInfo.Url https://.../logo.png \
    --FileInfos.4.Id aud \
    --FileInfos.4.InputInfo.Type URL \
    --FileInfos.4.InputInfo.UrlInputInfo.Url .../back_music.mp3 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket your_bucket \
    --OutputStorage.CosOutputStorage.Region your_bucket_region \
    --OutputObjectPath /your/output/dir/ \
    --ComposeConfig.TargetInfo.Container mp4 \
    --ComposeConfig.TargetInfo.VideoStream.Fps 30 \
    --ComposeConfig.Styles.0.Id ss \
    --ComposeConfig.Styles.0.Type Subtitle \
    --ComposeConfig.Styles.0.Subtitle.MarginBottom 50% \
    --ComposeConfig.Styles.0.Subtitle.FontType SimHei \
    --ComposeConfig.Styles.0.Subtitle.FontSize 8% \
    --ComposeConfig.Styles.0.Subtitle.FontBold 1 \
    --ComposeConfig.Styles.0.Subtitle.FontColor #FF0000FF \
    --ComposeConfig.Styles.0.Subtitle.BorderWidth 2px \
    --ComposeConfig.Styles.0.Subtitle.BorderColor #00FF00FF \
    --ComposeConfig.Styles.0.Subtitle.BottomColor #0000FFFF \
    --ComposeConfig.Tracks.0.Type Title \
    --ComposeConfig.Tracks.0.Items.0.Type Subtitle \
    --ComposeConfig.Tracks.0.Items.0.Subtitle.StyleId ss \
    --ComposeConfig.Tracks.0.Items.0.Subtitle.TrackTime.Start 0s \
    --ComposeConfig.Tracks.0.Items.0.Subtitle.TrackTime.Duration 2s \
    --ComposeConfig.Tracks.0.Items.0.Subtitle.Text 片头-示例 \
    --ComposeConfig.Tracks.0.Items.1.Type Subtitle \
    --ComposeConfig.Tracks.0.Items.1.Subtitle.StyleId ss \
    --ComposeConfig.Tracks.0.Items.1.Subtitle.TrackTime.Start 2s \
    --ComposeConfig.Tracks.0.Items.1.Subtitle.TrackTime.Duration 8s \
    --ComposeConfig.Tracks.0.Items.1.Subtitle.Text 正片-示例 \
    --ComposeConfig.Tracks.0.Items.2.Type Subtitle \
    --ComposeConfig.Tracks.0.Items.2.Subtitle.StyleId ss \
    --ComposeConfig.Tracks.0.Items.2.Subtitle.TrackTime.Start 12s \
    --ComposeConfig.Tracks.0.Items.2.Subtitle.TrackTime.Duration 2s \
    --ComposeConfig.Tracks.0.Items.2.Subtitle.Text 片尾-示例 \
    --ComposeConfig.Tracks.1.Type Video \
    --ComposeConfig.Tracks.1.Items.0.Type Image \
    --ComposeConfig.Tracks.1.Items.0.Image.SourceMedia.FileId img \
    --ComposeConfig.Tracks.1.Items.0.Image.TrackTime.Duration 14s \
    --ComposeConfig.Tracks.1.Items.0.Image.XPos 85% \
    --ComposeConfig.Tracks.1.Items.0.Image.YPos 10% \
    --ComposeConfig.Tracks.1.Items.0.Image.Width 15% \
    --ComposeConfig.Tracks.2.Type Video \
    --ComposeConfig.Tracks.2.Items.0.Type Video \
    --ComposeConfig.Tracks.2.Items.0.Video.SourceMedia.FileId start \
    --ComposeConfig.Tracks.2.Items.0.Video.AudioOperations.0.Type Volume \
    --ComposeConfig.Tracks.2.Items.0.Video.AudioOperations.0.Volume 0.0 \
    --ComposeConfig.Tracks.2.Items.1.Type Video \
    --ComposeConfig.Tracks.2.Items.1.Video.SourceMedia.FileId video \
    --ComposeConfig.Tracks.2.Items.1.Video.SourceMedia.StartTime 10s \
    --ComposeConfig.Tracks.2.Items.1.Video.SourceMedia.EndTime 20s \
    --ComposeConfig.Tracks.2.Items.1.Video.AudioOperations.0.Type Volume \
    --ComposeConfig.Tracks.2.Items.1.Video.AudioOperations.0.Volume 0.0 \
    --ComposeConfig.Tracks.2.Items.2.Type Transition \
    --ComposeConfig.Tracks.2.Items.2.Transition.Transitions.0.Type Heart \
    --ComposeConfig.Tracks.2.Items.3.Type Image \
    --ComposeConfig.Tracks.2.Items.3.Image.SourceMedia.FileId end \
    --ComposeConfig.Tracks.2.Items.3.Image.TrackTime.Duration 3s \
    --ComposeConfig.Tracks.3.Type Audio \
    --ComposeConfig.Tracks.3.Items.0.Type Audio \
    --ComposeConfig.Tracks.3.Items.0.Audio.SourceMedia.FileId aud \
    --ComposeConfig.Tracks.3.Items.0.Audio.TrackTime.Duration 14s
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 4: 【合成任务】画中画**

将一个视频缩放，贴在另一个视频上面，合成一个新的视频。轨道形式如下：
<img width="30%" src="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/03_video_in_video/track.png" />

<a target="_blank" href="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/03_video_in_video/03_video_in_video.mp4">效果示例</a>


Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.Id back \
    --FileInfos.0.InputInfo.Type URL \
    --FileInfos.0.InputInfo.UrlInputInfo.Url https://.../video.mp4 \
    --FileInfos.1.Id over \
    --FileInfos.1.InputInfo.Type URL \
    --FileInfos.1.InputInfo.UrlInputInfo.Url https://.../over.mp4 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket your_bucket \
    --OutputStorage.CosOutputStorage.Region your_bucket_region \
    --OutputObjectPath /your/output/dir/ \
    --ComposeConfig.Tracks.0.Type Video \
    --ComposeConfig.Tracks.0.Items.0.Type Video \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.FileId over \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.StartTime 30s \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.EndTime 40s \
    --ComposeConfig.Tracks.0.Items.0.Video.AudioOperations.0.Type Volume \
    --ComposeConfig.Tracks.0.Items.0.Video.AudioOperations.0.Volume 0.0 \
    --ComposeConfig.Tracks.0.Items.0.Video.XPos 60% \
    --ComposeConfig.Tracks.0.Items.0.Video.YPos 30% \
    --ComposeConfig.Tracks.0.Items.0.Video.Width 300px \
    --ComposeConfig.Tracks.1.Type Video \
    --ComposeConfig.Tracks.1.Items.0.Type Video \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.FileId back \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.StartTime 10s \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.EndTime 20s
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 5: 【合成任务】视频倍速**

剪辑一个视频，前10s 两倍速播放，后10s 0.8倍数播放，合成一个新的视频。轨道形式如下：
<img width="40%" src="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/04_video_speed/track.png" />

<a target="_blank" href="https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/04_video_speed/04_video_speed.mp4">效果示例</a>

注：当元素 SourceMedia 里的素材时长和 TrackTime 时长不一致时，就能实现倍数。
注：倍速不能和转场同时使用。

Input: 

```
tccli mps EditMedia --cli-unfold-argument  \
    --FileInfos.0.Id vod \
    --FileInfos.0.InputInfo.Type URL \
    --FileInfos.0.InputInfo.UrlInputInfo.Url https://.../video.mp4 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket your_bucket \
    --OutputStorage.CosOutputStorage.Region your_bucket_region \
    --OutputObjectPath /your/output/dir/ \
    --ComposeConfig.Tracks.0.Type Video \
    --ComposeConfig.Tracks.0.Items.0.Type Video \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.FileId vod \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.StartTime 10s \
    --ComposeConfig.Tracks.0.Items.0.Video.SourceMedia.EndTime 20s \
    --ComposeConfig.Tracks.0.Items.0.Video.TrackTime.Duration 5s \
    --ComposeConfig.Tracks.1.Type Video \
    --ComposeConfig.Tracks.1.Items.0.Type Video \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.FileId vod \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.StartTime 20s \
    --ComposeConfig.Tracks.1.Items.0.Video.SourceMedia.EndTime 30s \
    --ComposeConfig.Tracks.1.Items.0.Video.TrackTime.Duration 12.5s
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx88-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

