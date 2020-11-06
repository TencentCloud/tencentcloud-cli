**Example 1: Initiating live steam audit task**

This example shows you how to initiate a content recognition task for a live stream whose URL is `http://www.abc.com/abc.m3u8`.

Input: 

```
tccli mps ProcessLiveStream --cli-unfold-argument  \
    --Url http://www.abc.com/abc.m3u8 \
    --TaskNotifyConfig.CmqModel Queue \
    --TaskNotifyConfig.CmqRegion gz \
    --TaskNotifyConfig.QueueName queue-125717729292 \
    --AiRecognitionTask.Definition 10
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

