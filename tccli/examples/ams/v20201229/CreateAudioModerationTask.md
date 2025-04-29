**Example 1: 创建音频审核任务**

创建音频审核任务

Input: 

```
tccli ams CreateAudioModerationTask --cli-unfold-argument  \
    --BizType default \
    --Type AUDIO \
    --Tasks.0.DataId 0a782332-c9db-4cf5-a66e-20d60b4ea469 \
    --Tasks.0.Input.Type URL \
    --Tasks.0.Input.Url https://test.myqcloud.com/test.mp3
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "DataId": "0a782332-c9db-4cf5-a66e-20d60b4ea469",
                "TaskId": "w-audio-aqwfdNiA4vq3Zysfa1",
                "Code": "OK",
                "Message": "Success"
            }
        ],
        "RequestId": "c933aca1-90d2-4ab8-b045-f1b08069d76f"
    }
}
```

