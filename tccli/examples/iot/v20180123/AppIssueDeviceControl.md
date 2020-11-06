**Example 1: 用户下发设备控制指令**

用户下发设备控制指令

Input: 

```
tccli iot AppIssueDeviceControl --cli-unfold-argument  \
    --AccessToken xxx \
    --ProductId iot-a8ojgbji \
    --DeviceName device \
    --ControlData {"light":"on"}
```

Output: 
```
{
    "Response": {
        "RequestId": "6b07242c-dd95-420f-9ab2-032eba5a49f0"
    }
}
```

