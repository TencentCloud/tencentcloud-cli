**Example 1: 查看任务详情**

在创建任务后，可以通过TaskId查看任务详情

Input: 

```
tccli vm DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-video-XwxJtbkKXWgCt8AZ
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
            "Duration": 36
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
                    "SubLabel": "",
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
                    "Url": "https://cos.ap-guangzhou.myqcloud.com/tianyu-live-video-content-moderation-1251001047/segment-/vod/w-video-ZN2GFtD0_xd2Zzvm/audio_0_1692239385.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIDHkrs3aFvAhCm8ery4ELZNw46TLvp-SVc5D2A5i1LaE-Rwc-RbzzNdnzIiKTyXklz%2F20230817%2Fap-guangzhou%2Fs3%2Faws4_request&amp;X-Amz-Date=20230817T022945Z&amp;X-Amz-Expires=43115&amp;X-Amz-Security-Token=RWPE9Op1vOCh8A4BcifIBS5tKQIEqp0a01534c752968ef2efea81d4768ed8420lwudsFkXv2-N4sxzTHZVtpU0X91sYbZAS23OP0L-QxCyO15HAZh3O0ja-wqkDP3XJ8FqSmj--JD4yeBE8IxDCPI8ns-GgfEKYxeOBHQLc38xGUi7jnAZHKa6oGXzqn-Mm4VFs7ankgd2AGR3gU-WVqSPaWecLwLcsfxpZL4_itLnVDfYOx3lRSu5D2Rs73E_ayevG4aFvZNYwSxEaajbbubUHM9BnA3dofrLpu16zyeFbt1nkgA7MaEYOmWHwuDTMfYqo5kdwikHIXID-kJC3rB4cyb9bJtGAMi_qZQcvWjipCiuhAJVVNz2m7JXXJ6uA7KJA1kFqVetnx2lGM3rQxjTG2I2sleVgFY1aky6dtNBfzCWSRguff0Z6LlfaNHh&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e86092a9bffeeea36a9d340021af6ae55681971ee7e1ac62ad347987a44fe5a2",
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
        "SegmentCosUrlList": {
            "ImageAllUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/image_all.json",
            "AudioAllUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/audio_all.json",
            "ImageBlockUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/image_block.json",
            "AudioBlockUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/audio_block.json",
            "AsrUrl": "https://tianyu-cms-ap-guangzhou-xxxx.cos.ap-guangzhou.myqcloud.com/segment-/video/w-video-ZN3KK99etTNyRHYu/asr_txt.json"
        },
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60",
        "ErrorType": "",
        "ErrorDescription": "",
        "Label": "Porn"
    }
}
```

