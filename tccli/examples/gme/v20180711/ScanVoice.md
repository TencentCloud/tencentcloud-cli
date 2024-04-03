**Example 1: 提交语音流检测任务**

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
                "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b"
            }
        ],
        "RequestId": "c91b5243-bbd1-48e0-af41-d66891cabecb"
    }
}
```

**Example 2: 提交语音文件检测任务**

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
                "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b"
            }
        ],
        "RequestId": "de52afb5-3887-462d-876a-f8b0b654dc92"
    }
}
```

**Example 3: 提交语音文件检测任务-2**

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
                "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b"
            }
        ],
        "RequestId": "c91b5243-bbd1-48e0-af41-d66891cabecb"
    }
}
```

