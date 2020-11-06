**Example 1: Submitting audio stream detection task**

This example shows you how to submit a speech detection task for an audio stream where the callback address is empty and the `DescribeScanResultList` API needs to be called to poll the detection result.

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --BizId 1400000000 \
    --Scenes default \
    --Live true \
    --Callback  \
    --Tasks.0.DataId 1400000000_test_data_id \
    --Tasks.0.Url https://xxxx
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

**Example 2: Submitting audio file detection task**

This example shows you how to submit a speech detection task for an audio file where the callback address (`Callback`) is set to get the detection result.

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --BizId 1400000000 \
    --Scenes default \
    --Live false \
    --Callback https://0.0.0.0/user_callback \
    --Tasks.0.DataId 1400000000_test_data_id \
    --Tasks.0.Url http://xxxx/audio_store/xxxx.mp3
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

**Example 3: Submitting audio file detection task**

This example shows you how to submit a speech detection task for an audio file where the callback address is empty and the `DescribeScanResultList` API needs to be called to poll the detection result.

Input: 

```
tccli gme ScanVoice --cli-unfold-argument  \
    --BizId 1400000000 \
    --Scenes default \
    --Live false \
    --Callback  \
    --Tasks.0.DataId 1400000000_test_data_id \
    --Tasks.0.Url http://xxx/audio_store/xxxx.mp3
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

