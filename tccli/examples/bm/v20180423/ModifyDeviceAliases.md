**Example 1: 修改服务器名称**



Input: 

```
tccli bm ModifyDeviceAliases --cli-unfold-argument  \
    --DeviceAliases.0.InstanceId tcpm-xxx0 \
    --DeviceAliases.0.Alias 名字1 \
    --DeviceAliases.1.InstanceId tcpm-xxx1 \
    --DeviceAliases.1.Alias 名字2
```

Output: 
```
{
    "Response": {
        "RequestId": "9716f8a4-5ef9-4cfe-93fd-573c2c699463"
    }
}
```

