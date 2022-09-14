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
                    "SubLabel": "",
                    "Suggestion": "Pass",
                    "Score": 0,
                    "Text": "测试音频文本",
                    "Url": "https://xxx.com/7c019/audio_0.mp3",
                    "Duration": "36398"
                },
                "OffsetTime": "0"
            }
        ],
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60",
        "ErrorType": "",
        "ErrorDescription": "",
        "TryInSeconds": 0,
        "Label": "Porn",
        "AudioText": "",
        "Asrs": []
    }
}
```

**Example 2: ok**



Input: 

```
tccli vm DescribeTaskDetail --cli-unfold-argument  \
    --ShowAllSegments true \
    --TaskId w-video-YyBIZHP6L4buPOcg
```

Output: 
```
{
    "Response": {
        "TaskId": "w-video-YyBIZHP6L4buPOcg",
        "DataId": "1111",
        "BizType": "default",
        "Name": "111",
        "Status": "RUNNING",
        "Type": "VIDEO",
        "Suggestion": "UNSPECIFIED",
        "Labels": [],
        "InputInfo": {
            "Type": "URL",
            "Url": "https://test-resources-1306254157.cos.ap-guangzhou.myqcloud.com/audio_policy_test/4%E5%88%86%E9%92%9F%E8%B6%85%E9%95%BF.m4a",
            "BucketInfo": null
        },
        "MediaInfo": {
            "Codecs": "",
            "Duration": 0,
            "Width": 0,
            "Height": 0,
            "Thumbnail": ""
        },
        "AudioText": "",
        "ImageSegments": [],
        "AudioSegments": [],
        "TryInSeconds": 0,
        "CreatedAt": "2022-09-13T09:07:48.926Z",
        "UpdatedAt": "2022-09-13T09:07:49.059Z",
        "ErrorType": "",
        "ErrorDescription": "",
        "Asrs": [],
        "Label": "",
        "RequestId": "ba257e71-a04b-4ba9-9d67-0717a39b6a96"
    }
}
```

**Example 3: vm详情返回示例**



Input: 

```
tccli vm DescribeTaskDetail --cli-unfold-argument  \
    --ShowAllSegments true \
    --TaskId w-live_audio-YyBybeJJPvjum5DP
```

Output: 
```
{
    "Response": {
        "TaskId": "w-live_audio-YyBybeJJPvjum5DP",
        "DataId": "1111",
        "BizType": "default",
        "Name": "111",
        "Status": "RUNNING",
        "Type": "LIVE_AUDIO",
        "Suggestion": "UNSPECIFIED",
        "Labels": [],
        "InputInfo": {
            "Type": "URL",
            "Url": "https://test-resources-1306254157.cos.ap-guangzhou.myqcloud.com/audio_policy_test/4%E5%88%86%E9%92%9F%E8%B6%85%E9%95%BF.m4a",
            "BucketInfo": null
        },
        "MediaInfo": {
            "Codecs": "",
            "Duration": 0,
            "Width": 0,
            "Height": 0,
            "Thumbnail": ""
        },
        "AudioText": "",
        "ImageSegments": [],
        "AudioSegments": [],
        "TryInSeconds": 120,
        "CreatedAt": "2022-09-13T12:07:09.338Z",
        "UpdatedAt": "2022-09-13T12:07:09.623Z",
        "ErrorType": "",
        "ErrorDescription": "",
        "Asrs": [],
        "Label": "",
        "RequestId": "08895eaa-2c51-4dc6-94fc-7b9bad51632b"
    }
}
```

