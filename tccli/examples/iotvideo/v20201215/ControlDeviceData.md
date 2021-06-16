**Example 1: 设置设备数据**

设置设备数据

Input: 

```
tccli iotvideo ControlDeviceData --cli-unfold-argument  \
    --ProductId LJ0INDNU7U \
    --DeviceName light1 \
    --Data {"brightness":1}
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

