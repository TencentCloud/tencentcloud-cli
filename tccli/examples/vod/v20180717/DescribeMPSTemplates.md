**Example 1: 获取指定 MPS 任务的参数模板**



Input: 

```
tccli vod DescribeMPSTemplates --cli-unfold-argument  \
    --SubAppId 221157 \
    --TemplateType SmartSubtitle
```

Output: 
```
{
    "Response": {
        "MPSTemplateSet": [
            {
                "MPSTemplateInfo": "{\"Definition\":100,\"Name\":\"ASR_中文源视频-生成中文字幕\",\"Comment\":\"\",\"Type\":\"Preset\",\"AsrHotWordsConfigure\":{\"Switch\":\"OFF\",\"LibraryId\":\"\"},\"AsrHotWordsLibraryName\":\"\",\"VideoSrcLanguage\":\"zh\",\"SubtitleFormat\":\"vtt\",\"SubtitleType\":0,\"TranslateSwitch\":\"OFF\",\"TranslateDstLanguage\":\"\",\"CreateTime\":\"2025-03-12T19:32:31+08:00\",\"UpdateTime\":\"2025-12-15T10:39:15+08:00\",\"AliasName\":\"ASR_Generate_Chinese_Subtitle_For_Chinese_Video\",\"ProcessType\":0,\"SelectingSubtitleAreasConfig\":{},\"SubtitleEmbedId\":0,\"SpeakerMode\":0,\"SpeakerLabel\":0}",
                "TaskType": "SmartSubtitle"
            }
        ],
        "TotalCount": 99,
        "RequestId": "33deb599-d221-4bab-95c9-76a203a06d24"
    }
}
```

