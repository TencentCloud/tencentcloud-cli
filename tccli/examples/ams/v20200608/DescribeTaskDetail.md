**Example 1: 查看任务详情**

在创建任务后，可以通过TaskId查看任务详情

Input: 

```
tccli ams DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-audio-Xw0mjnmaiu-Uv1fs
```

Output: 
```
{
    "Response": {
        "TaskId": "task-audio-XwxJtbkKXWgCt8AZ",
        "DataId": "data_test_01",
        "BizType": "1001",
        "Name": "",
        "Status": "FINISH",
        "Type": "AUDIO",
        "Suggestion": "Pass",
        "AudioText": "识别的音频文本",
        "MediaInfo": {
            "Codecs": "aac",
            "Duration": 36
        },
        "InputInfo": {
            "Type": "URL",
            "Url": "https://cms-video-segments-1256309736.cos.ap-guangzhou.myqcloud.co/huang.mp3"
        },
        "CreatedAt": "2020-07-13T11:47:01.925Z",
        "UpdatedAt": "2020-07-13T11:47:25.840Z",
        "TryInSeconds": 10,
        "AudioSegments": [
            {
                "Result": {
                    "HitFlag": 0,
                    "Label": "Normal",
                    "Suggestion": "Pass",
                    "Score": 0,
                    "Text": "Breaking har gre a king har Mo ni ou。来给生活比个月。更多的承诺。",
                    "Url": "https://xxx.com/7c019/audio_0.mp3",
                    "Duration": "36398"
                },
                "OffsetTime": "0"
            }
        ],
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60"
    }
}
```

