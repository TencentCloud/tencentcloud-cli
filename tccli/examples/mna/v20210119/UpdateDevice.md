**Example 1: 更新设备**

更新设备

Input: 

```
tccli mna UpdateDevice --cli-unfold-argument  \
    --DeviceId mna-yesydf \
    --DeviceName name1 \
    --Remark remarks \
    --UpdateNetInfo.0.Type 0 \
    --UpdateNetInfo.0.DataEnable True \
    --UpdateNetInfo.0.UploadLimit 1 \
    --UpdateNetInfo.0.DownloadLimit 1 \
    --UpdateNetInfo.0.NetInfoName netname
```

Output: 
```
{
    "Response": {
        "RequestId": "a400ac72-8f93-4340-a862-f74b56942703"
    }
}
```

