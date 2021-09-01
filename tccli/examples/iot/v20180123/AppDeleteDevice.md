**Example 1: 用户解绑设备**

用户解绑设备

Input: 

```
tccli iot AppDeleteDevice --cli-unfold-argument  \
    --AccessToken xxx \
    --ProductId iot-a8ojgbji \
    --DeviceName device
```

Output: 
```
{
    "Response": {
        "RequestId": "6b07242c-dd95-420f-9ab2-032eba5a49f0"
    }
}
```

