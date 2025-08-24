**Example 1: 查询 TWeSee 语义理解任务**



Input: 

```
tccli iotexplorer DescribeTWeSeeRecognitionTask --cli-unfold-argument  \
    --TaskId 01985f3b-1781-75e6-aed5-d6510855f086
```

Output: 
```
{
    "Response": {
        "RequestId": "a8632226-fe3c-4f70-86d9-eb995cefeae8",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1753944365,
            "DeviceName": "dev002",
            "EndTime": 1753944365,
            "EndTimeMs": 1753944365774,
            "Files": [],
            "FilesInfo": [],
            "ProductId": "4AHMY9X89Y",
            "Result": {
                "DetectedClassifications": [
                    "person",
                    "vehicle"
                ],
                "Status": 3,
                "Summary": "一穿蓝上衣的人驾驶蓝卡车在道路上行驶。"
            },
            "StartTime": 1753944364,
            "StartTimeMs": 1753944364774,
            "Status": 3,
            "TaskId": "01985f3b-1781-75e6-aed5-d6510855f086",
            "UpdateTime": 1753944368
        }
    }
}
```

