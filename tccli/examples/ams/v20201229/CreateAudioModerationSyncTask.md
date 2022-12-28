**Example 1: 音频同步接口返回示例**



Input: 

```
tccli ams CreateAudioModerationSyncTask --cli-unfold-argument  \
    --BizType test_biztype \
    --FileUrl https://test.myqcloud.com/test.mp3 \
    --DataId test0000000000001 \
    --Name test_file \
    --FileFormat mp3
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DataId": "test0000000000001",
        "Label": "Normal",
        "SubLabel": "",
        "Name": "test_audio",
        "BizType": "test_biztype",
        "Suggestion": "Pass",
        "AsrText": "新年快乐，恭喜发财，身体健康，万事如意。",
        "TextResults": [
            {
                "Label": "Normal",
                "Score": 0,
                "Keywords": 0,
                "Suggestion": "Pass",
                "LibId": "",
                "LibType": 0,
                "LibName": "",
                "SubLabel": ""
            }
        ],
        "MoanResults": [],
        "LanguageResults": [],
        "SpeakerResults": [],
        "RecognitionResults": [],
        "Duration": "15000"
    }
}
```

