**Example 1: 批量禁用启用设备**

批量禁用启用设备

Input: 

```
tccli iotexplorer UpdateDevicesEnableState --cli-unfold-argument  \
    --Status 1 \
    --DevicesItems.0.DeviceName d1 \
    --DevicesItems.0.ProductId Rf56GH9
```

Output: 
```
{
    "Response": {
        "ResultCode": "delete error",
        "ResultMessage": "delete error",
        "RequestId": "34edc-7ugf4rb-657uj"
    }
}
```

