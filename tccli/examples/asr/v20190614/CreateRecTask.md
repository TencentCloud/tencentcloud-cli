**Example 1: 通过音频Url来调用接口**

用户通过音频Url的方式（SourceType为0）请求录音识别服务，请求模型为16k中文 （EngineModelType = 16k_zh），音频格式为wav（采样率为16k，单声道）

Input: 

```
tccli asr CreateRecTask --cli-unfold-argument  \
    --Url http://test.cos.ap-guangzhou.myqcloud.com/test.wav \
    --ChannelNum 1 \
    --EngineModelType 16k_zh \
    --ResTextFormat 0 \
    --SourceType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": {
            "TaskId": 1393265
        }
    }
}
```

**Example 2: 通过音频数据来调用接口**

用户通过上传音频数据（Data）的方式（SourceType为1）请求录音识别服务，请求模型为16k中文 （EngineModelType = 16k_zh），音频格式为wav（采样率为16k，单声道）

Input: 

```
tccli asr CreateRecTask --cli-unfold-argument  \
    --ChannelNum 1 \
    --EngineModelType 16k_zh \
    --ResTextFormat 0 \
    --Data eGNmYXNkZmFzZmFzZGZhc2RmCg== \
    --SourceType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": {
            "TaskId": 1396665
        }
    }
}
```

