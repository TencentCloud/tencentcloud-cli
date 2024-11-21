**Example 1: 创建任务成功**

创建视频人像分割处理任务成功

Input: 

```
tccli bda CreateSegmentationTask --cli-unfold-argument  \
    --VideoUrl https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input.mp4 \
    --BackgroundImageUrl https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "RequestId": "33c35bff-27b6-408f-9ca7-19191303fa07",
        "TaskID": "12433580546999611111",
        "EstimatedProcessingTime": 30
    }
}
```

