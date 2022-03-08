**Example 1: 创建通知渠道组**



Input: 

```
tccli cls CreateAlarmNotice --cli-unfold-argument  \
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
        "AlarmNoticeId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

