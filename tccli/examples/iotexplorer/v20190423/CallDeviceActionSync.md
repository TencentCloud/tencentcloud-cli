**Example 1: 同步调用设备行为**

同步调用设备行为，返回调用结果。

Input: 

```
tccli iotexplorer CallDeviceActionSync --cli-unfold-argument  \
    --ProductId TOIDHQ3AOQ \
    --DeviceName light1 \
    --ActionId actid \
    --InputParams {"vol":3}
```

Output: 
```
{
    "Response": {
        "ClientToken": "0fe1260b7a724b67ba873ca7df703e0d",
        "OutputParams": "{\"brightness\":1,\"color\":1,\"light_switch\":1}",
        "RequestId": "235fe48b-0c31-4a7c-aaf6-83ba3e9s4bcf",
        "Status": "succ"
    }
}
```

