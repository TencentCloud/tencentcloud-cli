**Example 1: 查看任务详情**

在创建任务后，可以通过TaskId查看任务详情

Input: 

```
tccli ams DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-video-XwxJtbkKXWgCt8AZ
```

Output: 
```
{
    "Response": {
        "TaskId": "w-audio-ZxisIxxxxiui72wo",
        "DataId": "55xxx32_30496167",
        "BizType": "audio_test_xmly",
        "Name": "55xxx32_30496167.flv",
        "Status": "FINISH",
        "Type": "AUDIO",
        "Suggestion": "Block",
        "Labels": [
            {
                "Label": "Porn",
                "Suggestion": "Block",
                "Score": 99,
                "SubLabel": "SexualBehavior"
            }
        ],
        "InputInfo": {
            "Type": "URL",
            "Url": "https://cms.myqcloud.com/audio/test.flv",
            "BucketInfo": {
                "Bucket": "null",
                "Region": "null",
                "Object": "null"
            }
        },
        "AudioText": "测试音频文本",
        "AudioSegments": [
            {
                "OffsetTime": "30",
                "Result": {
                    "HitFlag": 1,
                    "Label": "Porn",
                    "Suggestion": "Block",
                    "Score": 95,
                    "Text": "测试音频文本",
                    "Url": "https://cms.myqcloud.com/audio/test.flv",
                    "Duration": "29000",
                    "Extra": "",
                    "TextResults": [
                        {
                            "Label": "Porn",
                            "Keywords": [
                                ""
                            ],
                            "LibId": "",
                            "LibName": "0",
                            "Score": 0,
                            "Suggestion": "Block",
                            "LibType": 0,
                            "SubLabel": "SexualBehavior"
                        }
                    ],
                    "MoanResults": [
                        {
                            "Label": "Moan",
                            "Score": 0,
                            "StartTime": 0,
                            "EndTime": 29,
                            "SubLabelCode": "",
                            "SubLabel": "",
                            "Suggestion": "Pass"
                        }
                    ],
                    "LanguageResults": [
                        {
                            "Label": "cmn",
                            "Score": 99,
                            "StartTime": 0,
                            "EndTime": 29,
                            "SubLabelCode": ""
                        }
                    ],
                    "SpeakerResults": [],
                    "LabelResults": [],
                    "TravelResults": [],
                    "SubLabel": "SexualBehavior",
                    "RecognitionResults": []
                }
            }
        ],
        "ErrorType": "",
        "ErrorDescription": "",
        "CreatedAt": "2024-10-23T07:56:17.008Z",
        "UpdatedAt": "2024-10-23T07:58:01.441Z",
        "Label": "Porn",
        "RequestId": "26cada43-6e79-4xxx-b77d-636347cd5637"
    }
}
```

