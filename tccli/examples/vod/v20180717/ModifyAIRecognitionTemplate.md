**Example 1: 关闭视频片头片尾识别任务**

修改自定义音视频内容识别模板，关闭视频片头片尾识别任务。

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --HeadTailConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 同时关闭和开启一项识别任务**

修改自定义音视频内容识别模板，关闭视频片头片尾识别任务，开启视频拆条任务。

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --SegmentConfigure.Switch ON \
    --HeadTailConfigure.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 3: 修改内容识别截帧间隔时间**

修改自定义智能识别模板，将截帧间隔修改为 0.5 秒。

Input: 

```
tccli vod ModifyAIRecognitionTemplate --cli-unfold-argument  \
    --Definition 30 \
    --ScreenshotInterval 0.5
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

