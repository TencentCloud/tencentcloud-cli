**Example 1: 提交语音文件检测任务-2**

通过语音文件的方式提交检测任务，回调地址为空，需要通过接口(查询语音检测结果)主动轮询获取检测结果

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --Callback https://0.0.0.0/user_callback \
    --Live false \
    --Tasks.0.Url http://xxx/audio_store/xxxx.mp3 \
    --Tasks.0.DataId 1400000000_test_data_id \
    --BizId 1400000000 \
    --Scenes default
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DataId": "1400000000_test_data_id",
                "TaskId": "xxx-xxx-xxx"
            }
        ],
        "RequestId": "xxx-xxx-xxx"
    }
}
```

**Example 2: 提交语音流检测任务**

通过语音流的方式提交检测任务，回调地址为空，需要通过接口(查询语音检测结果)主动轮询获取检测结果

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --Callback https://0.0.0.0/user_callback \
    --Live true \
    --Tasks.0.Url https://xxxx \
    --Tasks.0.DataId 1400000000_test_data_id \
    --BizId 1400000000 \
    --Scenes default
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DataId": "1400000000_test_data_id",
                "TaskId": "xxx-xxx-xxx"
            }
        ],
        "RequestId": "xxx-xxx-xxx"
    }
}
```

**Example 3: 提交语音文件检测任务**

通过语音文件的方式提交检测任务，可通过设置回调地址 Callback 获取检测结果

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --Callback https://0.0.0.0/user_callback \
    --Live false \
    --Tasks.0.Url http://xxxx/audio_store/xxxx.mp3 \
    --Tasks.0.DataId 1400000000_test_data_id \
    --BizId 1400000000 \
    --Scenes default
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DataId": "1400000000_test_data_id",
                "TaskId": "xxx-xxx-xxx"
            }
        ],
        "RequestId": "xxx-xxx-xxx"
    }
}
```

