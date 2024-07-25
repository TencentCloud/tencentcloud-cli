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
        "TaskId": "abc",
        "DataId": "abc",
        "BizType": "abc",
        "Name": "abc",
        "Status": "abc",
        "Type": "abc",
        "Suggestion": "abc",
        "Labels": [
            {
                "Label": "abc",
                "Suggestion": "abc",
                "Score": 0,
                "SubLabel": "abc"
            }
        ],
        "InputInfo": {
            "Type": "abc",
            "Url": "abc",
            "BucketInfo": {
                "Bucket": "abc",
                "Region": "abc",
                "Object": "abc"
            }
        },
        "AudioText": "abc",
        "AudioSegments": [
            {
                "OffsetTime": "abc",
                "Result": {
                    "HitFlag": 0,
                    "Label": "abc",
                    "Suggestion": "abc",
                    "Score": 0,
                    "Text": "abc",
                    "Url": "abc",
                    "Duration": "abc",
                    "Extra": "abc",
                    "TextResults": [
                        {
                            "Label": "abc",
                            "Keywords": [
                                "abc"
                            ],
                            "LibId": "abc",
                            "LibName": "abc",
                            "Score": 0,
                            "Suggestion": "abc",
                            "LibType": 0,
                            "SubLabel": "abc"
                        }
                    ],
                    "MoanResults": [
                        {
                            "Label": "abc",
                            "Score": 0,
                            "StartTime": 0,
                            "EndTime": 0,
                            "SubLabelCode": "abc",
                            "SubLabel": "abc",
                            "Suggestion": "abc"
                        }
                    ],
                    "LanguageResults": [
                        {
                            "Label": "abc",
                            "Score": 0,
                            "StartTime": 0,
                            "EndTime": 0,
                            "SubLabelCode": "abc"
                        }
                    ],
                    "SubLabel": "abc",
                    "RecognitionResults": [
                        {
                            "Label": "abc",
                            "Tags": [
                                {
                                    "Name": "abc",
                                    "Score": 0,
                                    "StartTime": 0,
                                    "EndTime": 0
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "ErrorType": "abc",
        "ErrorDescription": "abc",
        "CreatedAt": "abc",
        "UpdatedAt": "abc",
        "Label": "abc",
        "RequestId": "abc"
    }
}
```

