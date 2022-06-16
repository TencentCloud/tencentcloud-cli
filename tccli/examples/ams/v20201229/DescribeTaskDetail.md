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
        "TaskId": "w-audio-X_Qnzci_GulDQ01r",
        "DataId": "",
        "BizType": "202012161",
        "Name": "",
        "Status": "FINISH",
        "Type": "AUDIO",
        "Suggestion": "Review",
        "Labels": [
            {
                "Label": "Abuse",
                "Suggestion": "Review",
                "Score": 0,
                "SubLabel": ""
            }
        ],
        "InputInfo": {
            "Type": "URL",
            "Url": "https://test.cos.ap-guangzhou.myqcloud.com/porn5.mp3"
        },
        "AudioText": "音频文本",
        "AudioSegments": [
            {
                "Result": {
                    "HitFlag": 0,
                    "Url": "https://cos.ap-guangzhou.myqcloud.com/0.mp3",
                    "Suggestion": "Pass",
                    "Label": "Normal",
                    "Text": "",
                    "TextResults": [],
                    "MoanResults": [],
                    "LanguageResults": [],
                    "Duration": "60000",
                    "Score": 0,
                    "Extra": "",
                    "SubLabel": ""
                },
                "OffsetTime": "0"
            }
        ],
        "ErrorType": "",
        "ErrorDescription": "",
        "CreatedAt": "2021-01-05T08:48:13.069Z",
        "UpdatedAt": "2021-01-05T08:49:31.421Z",
        "RequestId": "34785328532523",
        "Label": "Abuse"
    }
}
```

