**Example 1: 请求示例1**



Input: 

```
tccli asr CreateAsyncRecognitionTask --cli-unfold-argument  \
    --EngineType 16k_zh \
    --Url http://tes.cos.ap-guangzhou.myqcloud.com/test.wav \
    --CallbackUrl http://test.com/callback \
    --SignToken 
```

Output: 
```
{
    "Response": {
        "RequestId": "fabc2d63-a1b7-40a0-b4c3-640f78974919",
        "Data": {
            "TaskId": 1000000007
        }
    }
}
```

