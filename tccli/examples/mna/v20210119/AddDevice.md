**Example 1: 新建设备**



Input: 

```
tccli mna AddDevice --cli-unfold-argument  \
    --DeviceName xxx \
    --Remark xxx \
    --DataKey xxx \
    --Encrypted false
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "DeviceId": "xx",
        "DataKey": "xxx",
        "Signature": "xxxx"
    }
}
```

