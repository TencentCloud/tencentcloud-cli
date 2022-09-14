**Example 1: 更新设备**



Input: 

```
tccli mna UpdateDevice --cli-unfold-argument  \
    --DeviceName xx \
    --Remark xx \
    --DeviceId mna-xxx \
    --UpdateNetInfo.0.DownloadLimit 100 \
    --UpdateNetInfo.0.UploadLimit 100 \
    --UpdateNetInfo.0.Type 0 \
    --UpdateNetInfo.0.DataEnable True \
    --UpdateNetInfo.0.NetInfoName xx \
    --UpdateNetInfo.1.Type 0 \
    --UpdateNetInfo.1.DataEnable True \
    --UpdateNetInfo.1.NetInfoName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "a400ac72-8f93-4340-a862-f74b56942703"
    }
}
```

