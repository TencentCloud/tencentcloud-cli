**Example 1: 修改直播流监播任务**

用户修改监播场次配置参数。

Input: 

```
tccli live ModifyLiveStreamMonitor --cli-unfold-argument  \
    --MonitorId abc \
    --MonitorName abc \
    --OutputInfo.OutputStreamName abc \
    --OutputInfo.OutputStreamWidth 1 \
    --OutputInfo.OutputStreamHeight 1 \
    --OutputInfo.OutputDomain abc \
    --OutputInfo.OutputApp abc \
    --InputList.0.InputStreamName abc \
    --InputList.0.InputDomain abc \
    --InputList.0.InputApp abc \
    --InputList.0.InputUrl abc \
    --InputList.0.Description abc \
    --NotifyPolicy.NotifyPolicyType 1 \
    --NotifyPolicy.CallbackUrl abc \
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

