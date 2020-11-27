**Example 1: 查询任务成功**

查询视频人像分割处理任务成功

Input: 

```
tccli bda DescribeSegmentationTask --cli-unfold-argument  \
    --TaskID taskID
```

Output: 
```
{
    "Response": {
        "RequestId": "0352ed67-66b0-4515-a04f-ddc0ab129658",
        "TaskStatus": "FINISHED",
        "ErrorMsg": "",
        "ResultVideoUrl": "http://resulturl.com/a.mp4",
        "ResultVideoMD5": "somemd5",
        "VideoBasicInformation": {
            "FrameWidth": 1280,
            "FrameHeight": 590,
            "FramesPerSecond": 28,
            "Duration": 21,
            "TotalFrames": 630
        }
    }
}
```

