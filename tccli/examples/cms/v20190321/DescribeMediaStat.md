**Example 1: 定制化接口音视频统计结果查询示例**



Input: 

```
tccli cms DescribeMediaStat --cli-unfold-argument  \
    --UserAppId 0 \
    --BizTypes xx \
    --UserSubUin xx \
    --MediaType xx \
    --StartTime xx \
    --UserUin xx \
    --EndTime xx
```

Output: 
```
{
    "Response": {
        "Summary": {
            "CreatedCount": "19",
            "ErrorCount": "0",
            "FinishCount": "18",
            "ImageSegCount": "167",
            "AudioDuration": "1732",
            "AudioSegCount": "96",
            "ResultStats": [
                {
                    "Suggestion": "Pass",
                    "Count": "7"
                },
                {
                    "Suggestion": "Review",
                    "Count": "0"
                },
                {
                    "Suggestion": "Block",
                    "Count": "11"
                }
            ],
            "LabelStats": [
                {
                    "Label": "Custom",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Polity",
                    "ReviewCount": "0",
                    "BlockCount": "3",
                    "TotalCount": "3"
                },
                {
                    "Label": "Porn",
                    "ReviewCount": "0",
                    "BlockCount": "2",
                    "TotalCount": "2"
                },
                {
                    "Label": "Moan",
                    "ReviewCount": "0",
                    "BlockCount": "2",
                    "TotalCount": "2"
                },
                {
                    "Label": "Terror",
                    "ReviewCount": "0",
                    "BlockCount": "2",
                    "TotalCount": "2"
                },
                {
                    "Label": "Illegal",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Religion",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Sexy",
                    "ReviewCount": "0",
                    "BlockCount": "2",
                    "TotalCount": "2"
                },
                {
                    "Label": "Abuse",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Ad",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Spam",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Teenager",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Copyright",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                },
                {
                    "Label": "Normal",
                    "ReviewCount": "0",
                    "BlockCount": "0",
                    "TotalCount": "0"
                }
            ]
        },
        "Details": [
            {
                "StatTime": "2021-08-03T16:00:00Z",
                "Stats": {
                    "CreatedCount": "19",
                    "ErrorCount": "0",
                    "FinishCount": "18",
                    "ImageSegCount": "167",
                    "AudioDuration": "1732",
                    "AudioSegCount": "96",
                    "ResultStats": [
                        {
                            "Suggestion": "Pass",
                            "Count": "7"
                        },
                        {
                            "Suggestion": "Review",
                            "Count": "0"
                        },
                        {
                            "Suggestion": "Block",
                            "Count": "11"
                        }
                    ],
                    "LabelStats": [
                        {
                            "Label": "Custom",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Polity",
                            "ReviewCount": "0",
                            "BlockCount": "3",
                            "TotalCount": "3"
                        },
                        {
                            "Label": "Porn",
                            "ReviewCount": "0",
                            "BlockCount": "2",
                            "TotalCount": "2"
                        },
                        {
                            "Label": "Moan",
                            "ReviewCount": "0",
                            "BlockCount": "2",
                            "TotalCount": "2"
                        },
                        {
                            "Label": "Terror",
                            "ReviewCount": "0",
                            "BlockCount": "2",
                            "TotalCount": "2"
                        },
                        {
                            "Label": "Illegal",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Religion",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Sexy",
                            "ReviewCount": "0",
                            "BlockCount": "2",
                            "TotalCount": "2"
                        },
                        {
                            "Label": "Abuse",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Ad",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Spam",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Teenager",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        },
                        {
                            "Label": "Copyright",
                            "ReviewCount": "0",
                            "BlockCount": "0",
                            "TotalCount": "0"
                        }
                    ]
                }
            }
        ],
        "RequestId": "c5c0451e-3bd6-4424-819b-5c747d7d0000"
    }
}
```

