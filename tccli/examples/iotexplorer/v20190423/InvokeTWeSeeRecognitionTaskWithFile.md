**Example 1: 上传文件并同步执行 TWeSee 语义理解任务 - 成功**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTaskWithFile --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --InputBase64 /9j/4AAQSkZJRgABAQAA...
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "Result": {
            "DetectedClassifications": [
                "vehicle"
            ],
            "Status": 3,
            "Summary": "一辆蓝色的货车在路边行驶"
        },
        "TaskId": "019a0fcc-0c9c-768f-9b7b-f2ff89972fd6",
        "RequestId": "ca9ade22-c2ec-49d6-9502-6397751a65f5"
    }
}
```

