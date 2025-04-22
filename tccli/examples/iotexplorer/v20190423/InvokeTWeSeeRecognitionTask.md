**Example 1: 同步执行 TWeSee 语义理解任务**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --InputURL hhttps://example.com/video.mp4 \
    --CustomId event-1 \
    --EnableSearch True \
    --StartTimeMs 1744389074077 \
    --EndTimeMs 1744389075077
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "RequestId": "26083bec-a7bd-491f-b6df-45e7f143638c",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "一个人在雨中行走"
        },
        "TaskId": "019625b1-15d6-72d8-a5d6-388b45c92c67"
    }
}
```

