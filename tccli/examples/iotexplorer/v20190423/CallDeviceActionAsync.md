**Example 1: 异步调用设备行为**

异步调用设备行为，返回调用 Id 信息。

Input: 

```
tccli iotexplorer CallDeviceActionAsync --cli-unfold-argument  \
    --ProductId TOIDHQ3AOQ \
    --DeviceName TOIDHQ2AOQ \
    --ActionId actid \
    --InputParams {"vol":3}
```

Output: 
```
{
    "Response": {
        "ClientToken": "45016a4535374abcb05e25790b916dc3",
        "RequestId": "235fe48b-0c31-4a7c-aaf6-83ba3e9b4bcf",
        "Status": "xx"
    }
}
```

