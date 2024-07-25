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
        "Total": "abc",
        "Data": [
            {
                "DataId": "abc",
                "TaskId": "abc",
                "Status": "abc",
                "Name": "abc",
                "BizType": "abc",
                "Type": "abc",
                "Suggestion": "abc",
                "MediaInfo": {
                    "Codecs": "abc",
                    "Duration": 0,
                    "Width": 0,
                    "Height": 0,
                    "Thumbnail": "abc"
                },
                "Labels": [
                    {
                        "Label": "abc",
                        "Suggestion": "abc",
                        "Score": 0,
                        "SubLabel": "abc"
                    }
                ],
                "CreatedAt": "abc",
                "UpdatedAt": "abc"
            }
        ],
        "PageToken": "abc",
        "RequestId": "abc"
    }
}
```

