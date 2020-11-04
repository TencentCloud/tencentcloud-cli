**Example 1: 设置设备数据-2**

设置设备数据

Input: 

```
tccli iotexplorer ControlDeviceData --cli-unfold-argument  \
    --ProductId LJ0INDNU7U\
    --DeviceName light1\
    --Data {"brightness":1}
```

Output: 
```
{
    "Response": {
        "Data": "",
        "RequestId": "5c982342-fb08-4fac-8e70-f63834667b52"
    }
}
```

**Example 2: 设置设备数据**

设置设备数据

Input: 

```
tccli iotexplorer ControlDeviceData --cli-unfold-argument  \
    --ProductId BKTTNGIQOG\
    --DeviceName dev01\
    --Data {"payload":"test","id":"abc"}
```

Output: 
```
{
    "Response": {
        "Data": "",
        "RequestId": "235fe48b-0c31-4a7c-aaf6-83ba3e9b4bcf",
        "Result": "{\"Sent\":1,\"pushResult\":0}"
    }
}
```

