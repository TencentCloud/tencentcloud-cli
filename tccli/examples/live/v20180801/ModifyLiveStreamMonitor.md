**Example 1: 修改直播流监播任务**

用户修改监播场次配置参数。

Input: 

```
tccli live ModifyLiveStreamMonitor --cli-unfold-argument  \
    --MonitorId caster-124 \
    --MonitorName caster-124 \
    --OutputInfo.OutputStreamName stream1 \
    --OutputInfo.OutputStreamWidth 1 \
    --OutputInfo.OutputStreamHeight 1 \
    --OutputInfo.OutputDomain  \
    --OutputInfo.OutputApp live \
    --InputList.0.InputStreamName stream2 \
    --InputList.0.InputDomain live.monitor.push.com \
    --InputList.0.InputApp live \
    --InputList.0.InputUrl rtmp://live.monitor.push.com/live/stream1 \
    --InputList.0.Description stream 1 \
    --NotifyPolicy.NotifyPolicyType 1 \
    --NotifyPolicy.CallbackUrl www.baidu.com \
    --AsrLanguage 1 \
    --OcrLanguage 1 \
    --AiAsrInputIndexList 1 \
    --AiOcrInputIndexList 1 \
    --CheckStreamBroken 1 \
    --CheckStreamLowFrameRate 1 \
    --AllowMonitorReport 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ff29075a-ef7a-4742-9268-f7a1980dafc5"
    }
}
```

