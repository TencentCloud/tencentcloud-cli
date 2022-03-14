**Example 1: 修改通知渠道组**



Input: 

```
tccli cls ModifyAlarmNotice --cli-unfold-argument  \
    --AlarmNoticeId notice-5b2ea996-4dae-47cc-bbad-5b12888b4c89 \
    --Name test \
    --Type All \
    --WebCallbacks.0.CallbackType Http \
    --WebCallbacks.0.Url http://www.testnotice.com/callback \
    --WebCallbacks.0.Method POST
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

