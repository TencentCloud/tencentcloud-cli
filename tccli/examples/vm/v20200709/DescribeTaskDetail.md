**Example 1: 查看任务详情**

在创建任务后，可以通过TaskId查看任务详情

Input: 

```
tccli vm DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-video-Xw0mjnmaiu-Uv1fs
```

Output: 
```
{
    "Response": {
        "TaskId": "task-video-XwxJtbkKXWgCt8AZ",
        "DataId": "data_test_01",
        "BizType": "1001",
        "Name": "",
        "Status": "FINISH",
        "Type": "VIDEO",
        "Suggestion": "Block",
        "Labels": [
            {
                "Label": "Porn",
                "Suggestion": "Block",
                "Score": 99
            },
            {
                "Label": "Hot",
                "Suggestion": "Block",
                "Score": 70
            }
        ],
        "MediaInfo": {
            "Codecs": "h264 aac",
            "Duration": 36,
            "Width": 352,
            "Height": 640
        },
        "InputInfo": {
            "Type": "URL",
            "Url": "https://cms-video-segments-1256309736.cos.ap-guangzhou.myqcloud.co/huang.mp4",
            "BucketInfo": null
        },
        "CreatedAt": "2020-07-13T11:47:01.925Z",
        "UpdatedAt": "2020-07-13T11:47:25.840Z",
        "TryInSeconds": 0,
        "ImageSegments": [
            {
                "Result": {
                    "HitFlag": 1,
                    "Label": "Porn",
                    "Suggestion": "Block",
                    "Score": 85,
                    "Results": [
                        {
                            "Scene": "Porn",
                            "HitFlag": 1,
                            "Suggestion": "Block",
                            "Label": "Porn",
                            "SubLabel": "",
                            "Score": 85,
                            "Names": [],
                            "Text": "",
                            "Details": []
                        }
                    ],
                    "Url": "https://cos.ap-zhou.myqcloud.com/c019/image_1.jpg"
                },
                "OffsetTime": "1"
            },
            {
                "Result": {
                    "HitFlag": 1,
                    "Label": "Porn",
                    "Suggestion": "Block",
                    "Score": 77,
                    "Results": [
                        {
                            "Scene": "Porn",
                            "HitFlag": 1,
                            "Suggestion": "Block",
                            "Label": "Porn",
                            "SubLabel": "",
                            "Score": 77,
                            "Names": [],
                            "Text": "",
                            "Details": []
                        }
                    ],
                    "Url": "https://cos.ap-guau.myqcloud.com/cc49b5b90a5d6802b7c019/image_2.jpg"
                },
                "OffsetTime": "2"
            }
        ],
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

