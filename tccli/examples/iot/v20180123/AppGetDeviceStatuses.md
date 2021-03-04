**Example 1: 批量获取绑定绑定设备状态**

批量获取绑定绑定设备状态

Input: 

```
tccli iot AppGetDeviceStatuses --cli-unfold-argument  \
    --AccessToken xxx \
    --DeviceIds ap-guangzhou/iot-a8ojgbji/abc ap-guangzhou/iot-a8ojgbji/aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "3fa7d395-c1ff-4ede-beec-59afdeded8e9",
        "DeviceStatuses": [
            {
                "DeviceId": "ap-guangzhou/iot-a8ojgbji&/abc",
                "Status": "offline"
            },
            {
                "DeviceId": "ap-guangzhou/iot-a8ojgbji&/aaa",
                "Status": "online"
            }
        ]
    }
}
```

