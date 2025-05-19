**Example 1: 发起任务**



Input: 

```
tccli mps BatchProcessMedia --cli-unfold-argument  \
    --InputInfo.0.Type URL \
    --InputInfo.0.UrlInputInfo.Url https://tetst-xxx-12xxxxx.cos.ap-xxxxx.myqcloud.com/processmedia/52.mp4 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket tetst-xxxx-125xxxxx \
    --OutputStorage.CosOutputStorage.Region ap-xxxxx \
    --OutputDir /output/ \
    --SmartSubtitlesTask.RawParameter.SubtitleType 2 \
    --SmartSubtitlesTask.RawParameter.VideoSrcLanguage zh \
    --SmartSubtitlesTask.RawParameter.SubtitleFormat vtt \
    --SmartSubtitlesTask.RawParameter.TranslateSwitch ON \
    --SmartSubtitlesTask.RawParameter.TranslateDstLanguage en \
    --TaskNotifyConfig.NotifyType URL \
    --TaskNotifyConfig.NotifyUrl http://xxxx.com/v2/push/mps_test?token=73YcsZyP \
    --SessionContext asdzxcs
```

Output: 
```
{
    "Response": {
        "RequestId": "b30891cd-cdc7-47db-94d3-4dbb85641dad",
        "TaskId": "24000030-BatchTask-e6fefa34fc497449c1a043b9a594c7det20"
    }
}
```

