**Example 1: 成功**

 

Input: 

```
tccli iss RefreshDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "12345678-abcd-efgh-ijkl-1234567890abcd"
    }
}
```

**Example 2: 设备未注册**

 

Input: 

```
tccli iss RefreshDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceUnavailable.DevNoRegister",
            "Message": "设备未注册"
        },
        "RequestId": "2b064fb2-a7b9-477a-a114-e3dcdeb2a132"
    }
}
```

