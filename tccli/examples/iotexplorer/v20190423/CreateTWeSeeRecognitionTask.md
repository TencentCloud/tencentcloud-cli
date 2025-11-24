**Example 1: 使用未创建的设备名创建视频摘要任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName not_exist_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --IsCustomDevice True \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "RequestId": "988080c5-b74a-4185-a404-f2877e08f97e",
        "TaskId": "0198cbc6-e472-79c6-953a-5240495d7640"
    }
}
```

**Example 2: 创建图片摘要任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/image.jpg \
    --InputType image \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "RequestId": "65dcf25f-385a-4b63-9a60-c99caa28f45a",
        "TaskId": "0198cbc8-8680-7b0a-bd4f-4dbff77853cd"
    }
}
```

**Example 3: 创建图片摘要任务（包含额外的事件行为检测）**

可选择的事件行为标签（SummaryConfig.DetectTypes）详见 [文档](https://cloud.tencent.com/document/api/1081/34988#VisionSummaryConfig)

Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/image.jpg \
    --InputType image \
    --ServiceType Summary \
    --SummaryConfig.DetectTypes baby_crying
```

Output: 
```
{
    "Response": {
        "TaskId": "019a77b8-e78a-7d75-82ae-596b969aae63",
        "RequestId": "f4256301-f72c-4eab-bcae-50548cbe987e"
    }
}
```

**Example 4: 创建目标检测任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --ServiceType ObjectDetect \
    --ObjectDetectConfig.DetectTypes adult child
```

Output: 
```
{
    "Response": {
        "RequestId": "57096151-fd04-4558-a2f9-280943e9682d",
        "TaskId": "0198cbc2-91df-79cd-96ca-0f73ef661632"
    }
}
```

**Example 5: 创建视频摘要任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "RequestId": "f3d7d0eb-d28d-43b0-9b8c-676f785edcb3",
        "TaskId": "0198cbc3-8c89-70f2-a07a-5a39b606bc92"
    }
}
```

**Example 6: 创建视频摘要任务且使该视频可被搜索**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --EnableSearch True \
    --StartTimeMs 1755765320366 \
    --EndTimeMs 1755765328366 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "RequestId": "c7a2ea4f-8a8c-484c-afde-c82005c643fb",
        "TaskId": "0198cbc4-eca1-78dd-b8ff-c150b97e081f"
    }
}
```

**Example 7: 创建视频摘要任务（包含多路摄像头的视频）**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --SummaryConfig.MultiCameraLayout Vertical,Num=2,Index=0;1 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "RequestId": "35044438-d9b8-42ee-a169-a40d9ecd96cc",
        "TaskId": "0198cbc5-e684-7335-a168-593d91d5d89f"
    }
}
```

