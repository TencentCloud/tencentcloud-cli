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
        "Status": "xx",
        "DataId": "xx",
        "ErrorType": "xx",
        "Name": "xx",
        "InputInfo": {
            "Url": "xx",
            "BucketInfo": "xx",
            "Type": "xx"
        },
        "BizType": "xx",
        "Labels": [
            {
                "Score": 99,
                "Suggestion": "xx",
                "Label": "xx"
            },
            {
                "Score": 70,
                "Suggestion": "xx",
                "Label": "xx"
            }
        ],
        "MediaInfo": {
            "Duration": 36,
            "Width": 352,
            "Height": 640,
            "Codecs": "xx"
        },
        "ImageSegments": [
            {
                "OffsetTime": "xx",
                "Result": {
                    "Extra": "xx",
                    "Url": "xx",
                    "Results": [
                        {
                            "Text": "xx",
                            "Scene": "xx",
                            "Label": "xx",
                            "SubLabel": "xx",
                            "Score": 85,
                            "Names": [
                                "xx"
                            ],
                            "Suggestion": "xx",
                            "HitFlag": 1,
                            "Details": [
                                {
                                    "LibName": "xx",
                                    "Name": "xx",
                                    "Text": "xx",
                                    "Score": 0,
                                    "Label": "xx",
                                    "SubLabelCode": "xx",
                                    "Location": {
                                        "Y": 0.0,
                                        "X": 0.0,
                                        "Rotate": 0.0,
                                        "Height": 0,
                                        "Width": 0
                                    },
                                    "Suggestion": "xx",
                                    "Keywords": [
                                        "xx"
                                    ],
                                    "LibId": "xx"
                                }
                            ]
                        }
                    ],
                    "Label": "xx",
                    "Score": 85,
                    "Suggestion": "xx",
                    "HitFlag": 1
                }
            },
            {
                "OffsetTime": "xx",
                "Result": {
                    "Extra": "xx",
                    "Url": "xx",
                    "Results": [
                        {
                            "Text": "xx",
                            "Scene": "xx",
                            "Label": "xx",
                            "SubLabel": "xx",
                            "Score": 77,
                            "Names": [
                                "xx"
                            ],
                            "Suggestion": "xx",
                            "HitFlag": 1,
                            "Details": [
                                {
                                    "SubLabelCode": "xx",
                                    "Name": "xx",
                                    "Text": "xx",
                                    "Score": 0,
                                    "Label": "xx",
                                    "LibName": "xx",
                                    "Location": {
                                        "Y": 0.0,
                                        "X": 0.0,
                                        "Rotate": 0.0,
                                        "Width": 0,
                                        "Height": 0
                                    },
                                    "Suggestion": "xx",
                                    "Keywords": [
                                        "xx"
                                    ],
                                    "LibId": "xx"
                                }
                            ]
                        }
                    ],
                    "Label": "xx",
                    "Score": 77,
                    "Suggestion": "xx",
                    "HitFlag": 1
                }
            }
        ],
        "TaskId": "xx",
        "AudioSegments": [
            {
                "OffsetTime": "xx",
                "Result": {
                    "TextResults": [
                        {
                            "LibName": "xx",
                            "Score": 0,
                            "Label": "xx",
                            "LibId": "xx",
                            "Suggestion": "xx",
                            "Keywords": [
                                "xx"
                            ],
                            "LibType": 0
                        }
                    ],
                    "Extra": "xx",
                    "Url": "xx",
                    "Text": "xx",
                    "MoanResults": [
                        {
                            "EndTime": 0.0,
                            "Score": 0,
                            "SubLabelCode": "xx",
                            "StartTime": 0.0,
                            "Label": "xx"
                        }
                    ],
                    "Label": "xx",
                    "Score": 0,
                    "Suggestion": "xx",
                    "Duration": "xx",
                    "HitFlag": 0,
                    "LanguageResults": [
                        {
                            "EndTime": 0.0,
                            "Score": 0,
                            "SubLabelCode": "xx",
                            "StartTime": 0.0,
                            "Label": "xx"
                        }
                    ]
                }
            }
        ],
        "Suggestion": "xx",
        "UpdatedAt": "xx",
        "TryInSeconds": 0,
        "Type": "xx",
        "ErrorDescription": "xx",
        "CreatedAt": "xx",
        "RequestId": "xx"
    }
}
```

