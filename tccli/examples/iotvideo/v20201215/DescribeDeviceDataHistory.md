**Example 1: 获取设备历史数据**



Input: 

```
tccli iotvideo DescribeDeviceDataHistory --cli-unfold-argument  \
    --ProductId TDCZ2WD29Z \
    --DeviceName DoNotDelete_34082530_1 \
    --MinTime 1612235965943 \
    --MaxTime 1612237765943 \
    --FieldName tencent_handsome
```

Output: 
```
{
    "Response": {
        "Context": "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAk0zcFnBpdzE2UUE4UlZ1UnFtTjhIeV81THcAAAAAAIscIRY2LTRMWW96VFQtQ3A5aDZFb043ZU5RAAAAAABnASsWaDVJZWNmbTJSNmlBckIyYy1mbEFVQQAAAAAAX2TnFl9CSDZsdnE1UkNpbmJ3U3lfNTVGX0EAAAAAAIKcqRZDTnp1RmZPNVFVR1pLMWF4Q3V5eDNR",
        "FieldName": "tencent_handsome",
        "Listover": true,
        "RequestId": "082a4de2-b0ec-4a8f-9f19-4fe08c887393",
        "Results": []
    }
}
```

