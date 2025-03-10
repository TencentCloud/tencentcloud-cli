**Example 1: 查询指定的云存 AI 分析任务**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceTask --cli-unfold-argument  \
    --TaskId fb066d7a-baac-4706-acda-058f56f82759
```

Output: 
```
{
    "Response": {
        "RequestId": "8b490930-d119-4ee2-963c-c58973a1ebe6",
        "TaskInfo": {
            "TaskId": "fb066d7a-baac-4706-acda-058f56f82759",
            "ProductId": "TQBDY6RPI9",
            "DeviceName": "cs_112114601_2",
            "ChannelId": 0,
            "ServiceType": "Highlight",
            "StartTime": 1710487888,
            "EndTime": 1710487898,
            "Status": 3,
            "Result": "",
            "Files": [
                "highlight.mp4",
                "thumbnail.jpg"
            ],
            "FilesInfo": [
                {
                    "FileName": "highlight.mp4"
                },
                {
                    "FileName": "thumbnail.mp4"
                }
            ],
            "CreateTime": 1710490000,
            "UpdateTime": 1710490000
        }
    }
}
```

