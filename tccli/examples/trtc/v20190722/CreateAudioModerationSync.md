**Example 1: 短音频内容理解同步接口**



Input: 

```
tccli trtc CreateAudioModerationSync --cli-unfold-argument  \
    --Sdkappid 140034324 \
    --DataId sdyfasdf \
    --FileFormat wav \
    --FileName testaudio.wav \
    --FileUrl https://sa201-oss-ugc-center.oss-cn-beijing.aliyuncs.com/hangtest/pkxkj22x902jILSIO28shxca/%E7%AC%AC%E4%B8%80%E6%89%B9%E6%B5%8B%E8%AF%95/%E9%9F%B3%E9%A2%91%E4%B8%8B%E8%BD%BD/29.wav
```

Output: 
```
{
    "Response": {
        "Audio": "",
        "AudioText": "求真务实，充分体现了马克思列宁主义，毛泽东思想，邓小平理论，三个代表重要思想和科学发展观的历史逻辑和内在联系。",
        "CheckDetail": [
            {
                "Desc": "涉政；核心领导",
                "Keywords": [
                    "毛泽东思想"
                ],
                "Label": "Polity",
                "LibName": "",
                "Scene": "",
                "Score": 100,
                "Severity": 0,
                "SeverityDesc": "",
                "SubLabel": "politics_coreleader",
                "Suggest": 2
            }
        ],
        "DataId": "sdyfasdf",
        "FileName": "testaudio.wav",
        "Label": "Polity",
        "MediaType": 1,
        "Rate": 100,
        "SubLabel": "politics_coreleader",
        "Suggest": 2,
        "TaskId": "636545579459027127",
        "RequestId": "0edb21fb-a9ac-4b0d-b12a-adf728d26980"
    }
}
```

