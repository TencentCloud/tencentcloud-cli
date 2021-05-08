**Example 1: 结构化对比查询接口示例**



Input: 

```
tccli cii DescribeStructCompareData --cli-unfold-argument  \
    --MainTaskId fybnnac89vk \
    --SubTaskId 
```

Output: 
```
{
    "Response": {
        "RequestId": "9317f6e4-6636-41a0-bf24-89ad9e4877f2",
        "PolicyId": "100001",
        "MainTaskId": "fybnnac89vk",
        "SubTaskId": "fybnnac89vl",
        "CustomerId": "100001",
        "CustomerName": "张三",
        "ReviewTime": "2020-12-19 18:43:37",
        "MachineResult": "{...}",
        "ManualResult": "{...}",
        "NewItems": "",
        "ModifyItems": "",
        "Metrics": {
            "ShortStructAccuracy": "95",
            "ShortStructRecall": "11",
            "LongStructAccuracy": "93",
            "LongStructRecall": "14",
            "LongContentAccuracy": "94",
            "LongContentRecall": "14"
        },
        "AllTasks": [
            {
                "MainTaskId": "fybnnac89vk",
                "SubTaskId": "fybnnac89vl",
                "TaskName": "体检报告",
                "TaskType": "HealthReport"
            }
        ],
        "TaskType": "BUltrasoundReport"
    }
}
```

