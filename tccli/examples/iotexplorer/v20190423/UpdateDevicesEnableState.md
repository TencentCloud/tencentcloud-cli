**Example 1: 批量禁用启用设备**

批量禁用启用设备

Input: 

```
tccli iotexplorer UpdateDevicesEnableState --cli-unfold-argument  \
    --Status 1 \
    --DevicesItems.0.DeviceName xx \
    --DevicesItems.0.ProductId xx
```

Output: 
```
{
    "Response": {
        "ResultCode": "xx",
        "ResultMessage": "xx",
        "RequestId": "xx"
    }
}
```

