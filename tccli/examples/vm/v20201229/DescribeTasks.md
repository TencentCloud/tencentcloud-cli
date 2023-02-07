**Example 1: 查看审核任务列表**

查看审核任务列表

Input: 

```
tccli vm DescribeTasks --cli-unfold-argument  \
    --Filter.Type VIDEO
```

Output: 
```
{
    "Response": {
        "Total": "1",
        "Data": [
            {
                "TaskId": "task-video-XwxJtbkKXWgCt8AZ",
                "DataId": "data_test_01",
                "BizType": "1001",
                "Name": "测试视频",
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
                    "Duration": 36
                },
                "InputInfo": {
                    "Type": "URL",
                    "Url": "https://cms.myqcloud.com/video/test.mp3",
                    "BucketInfo": null
                },
                "CreatedAt": "2020-07-13T11:47:01.925Z",
                "UpdatedAt": "2020-07-13T11:47:25.840Z"
            }
        ],
        "PageToken": "4765-48dXwxJtbkKXW8d3eb",
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60"
    }
}
```

