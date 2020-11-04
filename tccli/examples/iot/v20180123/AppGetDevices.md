**Example 1: 获取绑定设备列表**

获取绑定设备列表，用于在APP显示某个用户的绑定设备列表

Input: 

```
tccli iot AppGetDevices --cli-unfold-argument  \
    --AccessToken xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "2eb887d9-7a18-4569-be2e-d06db7c406ec",
        "Devices": [
            {
                "AliasName": "",
                "Region": "ap-guangzhou",
                "ProductId": "iot-a8ojgbji",
                "DeviceName": "ccc",
                "Id": "ap-guangzhou/iot-a8ojgbji/ccc"
            },
            {
                "AliasName": "",
                "Region": "ap-guangzhou",
                "ProductId": "iot-a8ojgbji",
                "DeviceName": "aaa",
                "Id": "ap-guangzhou/iot-a8ojgbji/aaa"
            }
        ]
    }
}
```

