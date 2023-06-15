**Example 1: 创建监播任务**

用户创建监播场次调用该接口。

Input: 

```
tccli live CreateLiveStreamMonitor --cli-unfold-argument  \
    --OutputInfo.OutputStreamWidth 1920 \
    --OutputInfo.OutputStreamHeight 1080 \
    --InputList.0.InputStreamName example
```

Output: 
```
{
    "Response": {
        "MonitorId": "3d5738dd-1ca2-4601-a6e9-004c5ec75c0b",
        "RequestId": "6c838ac2-a878-4609-bdc7-0145e4023340"
    }
}
```

