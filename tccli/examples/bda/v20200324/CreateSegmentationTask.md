**Example 1: 创建任务成功**

创建视频人像分割处理任务成功

Input: 

```
tccli bda CreateSegmentationTask --cli-unfold-argument  \
    --VideoUrl test.video.url \
    --BackgroundImageUrl test.image.url
```

Output: 
```
{
    "Response": {
        "RequestId": "33c35bff-27b6-408f-9ca7-19191303fa07",
        "TaskID": "fakeTaskID",
        "EstimatedProcessingTime": 30
    }
}
```

