**Example 1: 创建视频摘要任务并等待结果返回**

最大超时时间为 20 秒

Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "穿白衣服的人正在公园的小路上行走"
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 2: 创建视频摘要任务并等待结果返回（使该视频可被搜索）**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "穿白衣服的人正在公园的小路上行走"
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 3: 创建视频摘要任务并等待结果返回（使用未创建的设备名）**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "穿白衣服的人正在公园的小路上行走"
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 4: 创建图片摘要任务并等待结果返回**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "穿白衣服的人正在公园的小路上行走"
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 5: 创建视频摘要任务并等待结果返回（包含多路摄像头的视频）**



Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "person"
            ],
            "Status": 3,
            "Summary": "穿白衣服的人正在公园的小路上行走"
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 6: 创建目标检测任务并等待结果返回**

最大超时时间为 20 秒

Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
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
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "DetectedClassifications": [
                "adult"
            ],
            "Status": 3
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 7: 创建视频摘要任务后任务执行失败的情况**

下载/读取视频/图片失败时，返回 Status = 2，ErrorCode 字段指出具体错误原因

Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "Result": {
            "ErrorCode": "DownloadFailed",
            "Status": 2
        },
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

**Example 8: 创建视频摘要任务后任务执行超时的情况**

任务执行 20 秒仍未返回结果，返回 Completed = false，任务将继续执行，后续可凭 TaskId 通过 DescribeTWeSeeRecognitionTask 重新查询该任务的结果

Input: 

```
tccli iotexplorer InvokeTWeSeeRecognitionTask --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName example_device_name \
    --InputURL https://example.qq.com/video.mp4 \
    --ServiceType Summary
```

Output: 
```
{
    "Response": {
        "Completed": false,
        "RequestId": "dc51b72e-872d-4908-82c3-f2e2794f2f60",
        "TaskId": "0198cbcc-d65f-7606-b4ac-664381086005"
    }
}
```

