**Example 1: 查询指定的云存 AI 分析任务**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIServiceTask --cli-unfold-argument  \
    --TaskId c31aa4f2-08c9-4088-9603-186d7311fdd8
```

Output: 
```
{
    "Response": {
        "RequestId": "8b490930-d119-4ee2-963c-c58973a1ebe6",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1714240802,
            "DeviceName": "dev001",
            "EndTime": 1714233600,
            "Files": [
                "output.mp4"
            ],
            "ProductId": "TSLFHRWDSD",
            "Result": "",
            "ServiceType": "Highlight",
            "StartTime": 1714147200,
            "Status": 3,
            "TaskId": "c31aa4f2-08c9-4088-9603-186d7311fdd8",
            "UpdateTime": 1714240802
        }
    }
}
```

