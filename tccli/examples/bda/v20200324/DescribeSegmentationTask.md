**Example 1: 查询任务成功**

查询视频人像分割处理任务成功

Input: 

```
tccli bda DescribeSegmentationTask --cli-unfold-argument  \
    --TaskID 12433580546999111111
```

Output: 
```
{
    "Response": {
        "RequestId": "0352ed67-66b0-4515-a04f-ddc0ab129658",
        "TaskStatus": "FINISHED",
        "ErrorMsg": "",
        "ResultVideoUrl": "https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/result.mp4?q-sign-algorithm=sha1&q-ak=AKID********EXAMPLE&q-sign-time=8888;9999&q-key-time=8888;9999&q-header-list=&q-url-param-list=&q-signature=7de87f7bf9cfd23df9da32f46661e7cf97a5603c",
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

