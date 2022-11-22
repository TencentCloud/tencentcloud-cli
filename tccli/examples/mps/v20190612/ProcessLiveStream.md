**Example 1: 发起直播流识别任务**

对 URL 为 http://www.abc.com/abc.m3u8 的直播流发起内容识别任务。

Input: 

```
tccli mps ProcessLiveStream --cli-unfold-argument  \
    --Url http://www.abc.com/abc.m3u8 \
    --AiRecognitionTask.Definition 10 \
    --TaskNotifyConfig.CmqRegion gz \
    --TaskNotifyConfig.CmqModel Queue \
    --TaskNotifyConfig.QueueName queue-125717729292
```

Output: 
```
{
    "Response": {
        "RequestId": "5ca61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "TaskId": "125xxxxxx07-live-procedure-813dc41e6fdc22dcf24aa6e9c61cp92"
    }
}
```

