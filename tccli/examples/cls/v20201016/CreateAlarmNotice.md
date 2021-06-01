**Example 1: 创建告警通知模板**



Input: 

```
tccli cls CreateAlarmNotice --cli-unfold-argument  \
    --Name test \
    --Type All \
    --WebCallbacks.0.CallbackType Http \
    --WebCallbacks.0.Url http://www.testnotice.com/callback \
    --WebCallbacks.0.Method POST \
    --WebCallbacks.0.Headers Content-Type:appliction/json \
    --WebCallbacks.0.Body {"Uin":"${UIN}","AlarmId":"alarm-xxxxxxxxx"}
```

Output: 
```
{
    "Response": {
        "AlarmNoticeId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

