**Example 1: 查看审核任务列表**

查看审核任务列表

Input: 

```
tccli ams DescribeTasks --cli-unfold-argument  \
    --Filter.Type AUDIO
```

Output: 
```
{
    "Response": {
        "Total": "382",
        "Data": [
            {
                "DataId": "317xxx867800",
                "TaskId": "w-audio-xxxxx_ouZOdcjYeN",
                "Status": "FINISH",
                "Name": "test",
                "BizType": "audit_txxxxx_xmly",
                "Type": "AUDIO",
                "Suggestion": "Review",
                "MediaInfo": {
                    "Codecs": "",
                    "Duration": 177,
                    "Width": 0,
                    "Height": 0,
                    "Thumbnail": ""
                },
                "Labels": [
                    {
                        "Label": "Abuse",
                        "Suggestion": "Review",
                        "Score": 86,
                        "SubLabel": "Uncivilized"
                    }
                ],
                "InputInfo": {
                    "Type": "URL",
                    "Url": "https://xxxx.com",
                    "BucketInfo": null
                },
                "CreatedAt": "2024-10-23T08:41:07.947Z",
                "UpdatedAt": "2024-10-23T08:41:53.739Z"
            }
        ],
        "PageToken": ".Zxi2o_ouxxxxjYeN",
        "RequestId": "8172167d-8755-43d8-a7ce-76f3103059ac"
    }
}
```

