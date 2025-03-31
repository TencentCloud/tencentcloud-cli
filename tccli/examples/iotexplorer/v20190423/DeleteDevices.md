**Example 1: 批量删除设备**

批量删除设备

Input: 

```
tccli iotexplorer DeleteDevices --cli-unfold-argument  \
    --DevicesItems.0.DeviceName d1 \
    --DevicesItems.0.ProductId Uj9JF5R4
```

Output: 
```
{
    "Response": {
        "ResultCode": "fail",
        "ResultMessage": "device has binded family",
        "RequestId": "3edc-6yh0-8tghs"
    }
}
```

