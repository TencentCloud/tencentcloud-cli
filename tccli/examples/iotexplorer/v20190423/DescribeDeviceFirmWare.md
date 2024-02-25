**Example 1: 获取设备固件信息**

获取设备固件信息

Input: 

```
tccli iotexplorer DescribeDeviceFirmWare --cli-unfold-argument  \
    --ProductId R7NHIV278R \
    --DeviceName dev1
```

Output: 
```
{
    "Response": {
        "Data": "{\"DeviceLabel\":\"{}\",\"FwVer\":\"V3.0.1\",\"Imei\":\"11-22-33-44\",\"Mac\":\"\",\"ModuleHardinfo\":\"ESP8266\",\"ModuleSoftinfo\":\"V1.0\"}",
        "RequestId": "afd60755-55d5-430c-a833-734aa81ec264"
    }
}
```

