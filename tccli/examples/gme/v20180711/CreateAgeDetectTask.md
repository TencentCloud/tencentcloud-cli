**Example 1: 提交年龄语音识别任务**

提交年龄语音识别任务

Input: 

```
tccli gme CreateAgeDetectTask --cli-unfold-argument  \
    --BizId 123456 \
    --Callback https://xxx.com/callback \
    --Tasks.0.DataId 6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b \
    --Tasks.0.Url https://yy.com/xx.wav
```

Output: 
```
{
    "Response": {
        "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b",
        "RequestId": "ecefce57a9ae2087d0cbf7fcc0e27bac"
    }
}
```

