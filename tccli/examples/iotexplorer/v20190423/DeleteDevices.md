**Example 1: 批量删除设备**

批量删除设备

Input: 

```
tccli iotexplorer DeleteDevices --cli-unfold-argument  \
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

