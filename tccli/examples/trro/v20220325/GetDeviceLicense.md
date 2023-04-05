**Example 1: 获取设备license**

获取设备可用license数量

Input: 

```
tccli trro GetDeviceLicense --cli-unfold-argument  \
    --ProjectId abc \
    --DeviceId abc
```

Output: 
```
{
    "Response": {
        "AvailableCount": 12,
        "RequestId": "abc"
    }
}
```

