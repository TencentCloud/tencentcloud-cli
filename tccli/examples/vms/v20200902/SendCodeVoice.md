**Example 1: 发送语音验证码**

发送语音验证码

Input: 

```
tccli vms SendCodeVoice --cli-unfold-argument  \
    --CodeMessage 8253 \
    --PlayTimes 2 \
    --CalledNumber +8613788888888 \
    --SessionContext sc-t \
    --VoiceSdkAppid 1400006666
```

Output: 
```
{
    "Response": {
        "SendStatus": {
            "CallId": "12582bce-403c-11eb-96b8-525400476c37",
            "SessionContext": "sc-t"
        },
        "RequestId": "91260bb8-cf91-4f3e-a81f-9198114a2279"
    }
}
```

