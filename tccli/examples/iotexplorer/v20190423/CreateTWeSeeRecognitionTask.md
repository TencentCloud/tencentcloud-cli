**Example 1: 创建 TWeSee 语义理解任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "RequestId": "26083bec-a7bd-491f-b6df-45e7f143638c",
        "TaskId": "019625b1-15d6-72d8-a5d6-388b45c92c67"
    }
}
```

