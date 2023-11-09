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
                "Score": 99,
                "SubLabel": ""
            },
            {
                "Label": "Hot",
                "Suggestion": "Block",
                "Score": 70,
                "SubLabel": ""
            }
        ],
        "MediaInfo": {
            "Codecs": "h264 aac",
            "Duration": 36,
            "Width": 352,
            "Height": 640,
            "Thumbnail": ""
        },
        "InputInfo": {
            "Type": "URL",
            "Url": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/huang.mp4",
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
                    "Url": "https://cos.ap-zhou.myqcloud.com/c019/image_1.jpg",
                    "Extra": "{}"
                },
                "OffsetTime": "1"
            }
        ],
        "AudioSegments": [
            {
                "Result": {
                    "HitFlag": 1,
                    "Url": "https://cos.ap-guangzhou.myqcloud.com/xxx",
                    "Suggestion": "Block",
                    "Label": "Illegal",
                    "Text": "全民制作人们大家好，我是练习时长。",
                    "TextResults": [],
                    "MoanResults": [
                        {
                            "Label": "Moan",
                            "Score": 0,
                            "StartTime": 0,
                            "EndTime": 4000,
                            "Suggestion": "Pass",
                            "SubLabel": "",
                            "SubLabelCode": ""
                        }
                    ],
                    "LanguageResults": [],
                    "Duration": "4000",
                    "Score": 1,
                    "Extra": "{}",
                    "SubLabel": "Anthem",
                    "RecognitionResults": [
                        {
                            "Label": "Teenager",
                            "Tags": [
                                {
                                    "Name": "Teenager",
                                    "Score": 0,
                                    "StartTime": 0,
                                    "EndTime": 4050
                                }
                            ]
                        }
                    ]
                },
                "OffsetTime": "0"
            }
        ],
        "AudioText": "",
        "Asrs": [
            {
                "Text": "",
                "CreatedAt": ""
            }
        ],
        "SegmentCosUrlList": {
            "ImageAllUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/image_all.json",
            "AudioAllUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/audio_all.json",
            "ImageBlockUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/image_block.json",
            "AudioBlockUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/audio_block.json",
            "AsrUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/asr_txt.json"
        },
        "TryInSeconds": 0,
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60",
        "ErrorType": "",
        "ErrorDescription": "",
        "Label": "Porn"
    }
}
```

