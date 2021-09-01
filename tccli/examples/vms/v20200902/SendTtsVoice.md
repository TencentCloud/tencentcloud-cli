**Example 1: 指定模板发送语音通知**



Input: 

```
tccli vms SendTtsVoice --cli-unfold-argument  \
    --TemplateId 4356 \
    --TemplateParamSet 7652 \
    --PlayTimes 2 \
    --CalledNumber +8613788888888 \
    --SessionContext test \
    --VoiceSdkAppid 1400006666
```

Output: 
```
{
    "Response": {
        "SendStatus": {
            "CallId": "12582bce-403c-11eb-96b8-525400476c37",
            "SessionContext": "test"
        },
        "RequestId": "91260bb8-cf91-4f3e-a81f-9198114a2279"
    }
}
```

